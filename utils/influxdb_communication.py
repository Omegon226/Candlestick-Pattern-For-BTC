# Базовые библиотеки
import numpy as np
import pandas as pd
import datetime
# Библитеки для взаимодействия с БД
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
# Библиотека для получения данных о криптовалюте
import ccxt


# Доступные временные диапазоны для свечей
#TIMEFRAMES = ["5m", "15m", "30m", "1h", "2h", "4h", "8h", "12h", "1d"]
TIMEFRAMES = ["15m", "30m", "1h", "2h", "4h", "8h", "12h", "1d"]
# Шаг по времени в UNIX формате для считывания данных в БД (1000 * sec/min * min/hour * hour/day * 1000)
TIMEFRAMES_STEPS = {
    "5m": 300000000, "15m": 900000000, "30m": 1800000000, 
    "1h": 3600000000, "2h": 7200000000, "4h": 14400000000, 
    "8h": 28800000000, "12h": 43200000000, "1d": 86400000000
}
# Данные для работы с InfluxDB
INFLUXDB_URL = "http://influxdb:8086"
INFLUXDB_TOCKEN = "admin"
INFLUXDB_BUCKET = "admin"
INFLUXDB_ORG = "admin"
# Биржа из которой будут браться данные с помощью CCXT
EXCHANGE = ccxt.binance()
# С этого момента времени в формате UNIX будет считываться информация с биржи (2017-08-17 04:00:00)
FROM_TIMESTAMP = 1502942400000


def create_data(symbol: str, timeframe: str):
    try:
        print(f"Началась запись данных о {symbol} с таймфремом {timeframe} в InfluxDB", end="\n")
        # Подключение к InfluxDB
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOCKEN, org=INFLUXDB_ORG, debug=False)
        write_client = client.write_api(write_options=SYNCHRONOUS)

        # Константы для прохождения в цикле
        dataframe_len = 1
        counter = 0

        while dataframe_len > 0:
            # Получение и обработка данных с биржи
            ohlcv = EXCHANGE.fetch_ohlcv(symbol, timeframe, FROM_TIMESTAMP + TIMEFRAMES_STEPS[timeframe] * counter, 1000)
            ohlcv = pd.DataFrame(ohlcv, columns=["Date", "Open", "High", "Low", "Close", "Volume"])
            ohlcv["Date"] = ohlcv["Date"].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000))

            # Увеличиваем счётчик
            counter += 1
            # Получаем кол-во строк из полученных данных
            dataframe_len = ohlcv.shape[0]

            # Запись данных в InfluxDB
            write_client.write(
                bucket=INFLUXDB_BUCKET,
                record=ohlcv,
                data_frame_measurement_name=f"{symbol}_{timeframe}",
                data_frame_timestamp_column="Date",
            )

            print(f"\rКол-во записей в InfluxDB: {counter}", end="")

        # Закрытие подключения к InfluxDB
        client.close()

        print(f"\nЗапись данных о {symbol} с таймфремом {timeframe} в InfluxDB прошла успешно", end="\n"*3)
        
    except Exception as err:
        raise err


def create_all_timeframes_data(symbol: str):
    try:
        for timeframe in TIMEFRAMES:
            create_data(symbol, timeframe)

    except Exception as err:
        raise err


def read_data(symbol: str, timeframe: str):
    try:
        # Подключение к InfluxDB
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOCKEN, org=INFLUXDB_ORG, debug=False, timeout=60000)
        query_api = client.query_api()

        # Запрос в InfluxDB для получения данных в формате DataFrame
        query= f'''
        from(bucket: "{INFLUXDB_BUCKET}") 
        |> range(start: -10000d)
        |> filter(fn: (r) => r["_measurement"] == "{symbol}_{timeframe}")
        |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
        '''

        # Получение и обработка данных
        df = query_api.query_data_frame(query)
        df = df.drop(columns=["result", "table", "_start", "_stop", "_measurement"])
        df = df.rename(columns={"_time": "Date"})

        return df

    except Exception as err:
        raise err


def delete_all_data():
    try:
        # Подключение к InfluxDB
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOCKEN, org=INFLUXDB_ORG, debug=False, timeout=100000)
        delete_api = client.delete_api()

        # Удаление всех данных и бакета
        delete_api.delete(start="1970-01-01T00:00:00Z", stop="2099-12-31T23:59:59Z", predicate="", bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG)

        # Закрытие подключения к InfluxDB
        client.close()

    except Exception as err:
        raise err


def delete_measurement(measurement):
    try:
        # Подключение к InfluxDB
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOCKEN, org=INFLUXDB_ORG, debug=False, timeout=100000)
        delete_api = client.delete_api()

        # Удаление определенного measurement из бакета
        delete_api.delete("1970-01-01T00:00:00Z", "2099-12-31T23:59:59Z", f'_measurement="{measurement}"', bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG)

        # Закрытие подключения к InfluxDB
        client.close()

    except Exception as err:
        raise err


def add_caldel_patterns_data(data, symbol: str, timeframe: str):
    try:
        # Подключение к InfluxDB
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOCKEN, org=INFLUXDB_ORG, debug=False, timeout=100000)
        write_client = client.write_api(write_options=SYNCHRONOUS)

        # Запись данных в InfluxDB
        write_client.write(
            bucket=INFLUXDB_BUCKET,
            record=data.drop(columns=["Close", "High", "Low", "Open", "Volume"]),
            data_frame_measurement_name=f"{symbol}_{timeframe}_candel_patterns",
            data_frame_timestamp_column="Date",
        )

        # Закрытие подключения к InfluxDB
        client.close()

    except Exception as err:
        raise err


def query_data(query: str):
    try:
         # Подключение к InfluxDB
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOCKEN, org=INFLUXDB_ORG, debug=False, timeout=100000)
        query_api = client.query_api()

        # Отправка запроса в БД
        data = query_api.query(query)

        # Закрытие подключения к InfluxDB
        client.close()

        return data
    
    except Exception as err:
        raise err


def query_df(query: str):
    try:
        # Подключение к InfluxDB
        client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOCKEN, org=INFLUXDB_ORG, debug=False, timeout=100000)
        query_api = client.query_api()

        # Отправка запроса в БД
        df = query_api.query_data_frame(query)

        # Закрытие подключения к InfluxDB
        client.close()

        return df

    except Exception as err:
        raise err