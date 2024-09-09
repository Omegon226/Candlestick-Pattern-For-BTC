# Базовые библиотеки
import numpy as np
import pandas as pd
# Библиотека тех аланиза для свечных паттернов
import talib


# Расчёт всех возможных свечных паттернов
def add_all_caldel_patterns(ohlc):
    ohlc["CDL2CROWS"] = talib.CDL2CROWS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDL3BLACKCROWS"] = talib.CDL3BLACKCROWS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDL3INSIDE"] = talib.CDL3INSIDE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDL3LINESTRIKE"] = talib.CDL3LINESTRIKE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDL3OUTSIDE"] = talib.CDL3OUTSIDE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDL3STARSINSOUTH"] = talib.CDL3STARSINSOUTH(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDL3WHITESOLDIERS"] = talib.CDL3WHITESOLDIERS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLABANDONEDBABY"] = talib.CDLABANDONEDBABY(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLADVANCEBLOCK"] = talib.CDLADVANCEBLOCK(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLBELTHOLD"] = talib.CDLBELTHOLD(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLBREAKAWAY"] = talib.CDLBREAKAWAY(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLCLOSINGMARUBOZU"] = talib.CDLCLOSINGMARUBOZU(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLCONCEALBABYSWALL"] = talib.CDLCONCEALBABYSWALL(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLCOUNTERATTACK"] = talib.CDLCOUNTERATTACK(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLDARKCLOUDCOVER"] = talib.CDLDARKCLOUDCOVER(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLDOJI"] = talib.CDLDOJI(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLDOJISTAR"] = talib.CDLDOJISTAR(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLDRAGONFLYDOJI"] = talib.CDLDRAGONFLYDOJI(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLENGULFING"] = talib.CDLENGULFING(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLEVENINGDOJISTAR"] = talib.CDLEVENINGDOJISTAR(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLEVENINGSTAR"] = talib.CDLEVENINGSTAR(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLGAPSIDESIDEWHITE"] = talib.CDLGAPSIDESIDEWHITE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLGRAVESTONEDOJI"] = talib.CDLGRAVESTONEDOJI(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHAMMER"] = talib.CDLHAMMER(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHANGINGMAN"] = talib.CDLHANGINGMAN(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHARAMI"] = talib.CDLHARAMI(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHARAMICROSS"] = talib.CDLHARAMICROSS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHIGHWAVE"] = talib.CDLHIGHWAVE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHIKKAKE"] = talib.CDLHIKKAKE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHIKKAKEMOD"] = talib.CDLHIKKAKEMOD(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLHOMINGPIGEON"] = talib.CDLHOMINGPIGEON(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLIDENTICAL3CROWS"] = talib.CDLIDENTICAL3CROWS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLINNECK"] = talib.CDLINNECK(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLINVERTEDHAMMER"] = talib.CDLINVERTEDHAMMER(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLKICKING"] = talib.CDLKICKING(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLKICKINGBYLENGTH"] = talib.CDLKICKINGBYLENGTH(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLLADDERBOTTOM"] = talib.CDLLADDERBOTTOM(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLLONGLEGGEDDOJI"] = talib.CDLLONGLEGGEDDOJI(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLLONGLINE"] = talib.CDLLONGLINE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLMARUBOZU"] = talib.CDLMARUBOZU(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLMATCHINGLOW"] = talib.CDLMATCHINGLOW(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLMATHOLD"] = talib.CDLMATHOLD(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLMORNINGDOJISTAR"] = talib.CDLMORNINGDOJISTAR(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLMORNINGSTAR"] = talib.CDLMORNINGSTAR(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLONNECK"] = talib.CDLONNECK(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLPIERCING"] = talib.CDLPIERCING(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLRICKSHAWMAN"] = talib.CDLRICKSHAWMAN(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLRISEFALL3METHODS"] = talib.CDLRISEFALL3METHODS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLSEPARATINGLINES"] = talib.CDLSEPARATINGLINES(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLSHOOTINGSTAR"] = talib.CDLSHOOTINGSTAR(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLSHORTLINE"] = talib.CDLSHORTLINE(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLSPINNINGTOP"] = talib.CDLSPINNINGTOP(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLSTALLEDPATTERN"] = talib.CDLSTALLEDPATTERN(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLSTICKSANDWICH"] = talib.CDLSTICKSANDWICH(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLTAKURI"] = talib.CDLTAKURI(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLTASUKIGAP"] = talib.CDLTASUKIGAP(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLTHRUSTING"] = talib.CDLTHRUSTING(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLTRISTAR"] = talib.CDLTRISTAR(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLUNIQUE3RIVER"] = talib.CDLUNIQUE3RIVER(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLUPSIDEGAP2CROWS"] = talib.CDLUPSIDEGAP2CROWS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100
    ohlc["CDLXSIDEGAP3METHODS"] = talib.CDLXSIDEGAP3METHODS(ohlc['Open'], ohlc['High'], ohlc['Low'], ohlc['Close']) // 100

    return ohlc

