import http.client
import json

conn = http.client.HTTPSConnection("www.aa.com")
payload = json.dumps({
  "metadata": {
    "selectedProducts": [],
    "tripType": "OneWay",
    "udo": {
      "partner_code_info": "HY-R,CB2-Z,DIN-,MSC-MSC",
      "gd_treatment_code": "400001,400022,400112,500010,500012,500013,500014,503325,700002",
      "loyalty_tier": "Gold",
      "travel_type": "personal"
    }
  },
  "passengers": [
    {
      "type": "adult",
      "count": 1
    }
  ],
  "requestHeader": {
    "clientId": "AAcom"
  },
  "slices": [
    {
      "allCarriers": True,
      "cabin": "BUSINESS,FIRST",
      "departureDate": "2024-11-13",
      "destination": "JFK",
      "destinationNearbyAirports": False,
      "maxStops": None,
      "origin": "CTS",
      "originNearbyAirports": False
    }
  ],
  "tripOptions": {
    "corporateBooking": False,
    "fareType": "Lowest",
    "locale": "en_US",
    "pointOfSale": "US",
    "searchType": "Award"
  },
  "loyaltyInfo": None,
  "version": "",
  "queryParams": {
    "sliceIndex": 0,
    "sessionId": "",
    "solutionSet": "",
    "solutionId": ""
  }
})
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'cookie': 'QuantumMetricUserID=fac4f834457f80011242c58f18a6368d; _cc=AZNizTMj8f5WmWFwkokaxnVF; s_ecid=MCMID%7C21679992250229964980707030570960980556; tracker_device=eeef315b-671e-4236-b0b0-0652b5747833; OPTOUTMULTI=0:0%7Cc1:0%7Cc3:1; OPTCKMS=s; _cid_cc=AZNizTMj8f5WmWFwkokaxnVF; emcid=T-yjHa3pUIG; _ga_DBQRDJHHZC=GS1.1.1709692124.1.1.1709692146.38.0.0; _ga_XT7DLK33SZ=GS1.1.1709692124.1.1.1709692146.0.0.0; UAC=01971852dc504aa5bc8b08074c3cff59; cookie_banner=closed; hasCoachingModalDisplayed=true; rxVisitor=1681869701238GLKRAUJ0SM2ES4F85LSMG14CVTAFGUQ5; tracker_device_is_opt_in=true; _ga=GA1.1.1453946625.1709692125; _ga_PDJ1QT0KWT=GS1.1.1728480945.3.0.1728480945.60.0.0; aka_state_code=FL; aka_cr_code=US-FL; at_check=true; AMCVS_025C69945392449B0A490D4C%40AdobeOrg=1; s_cc=true; spa_session_id=9383dd35-2587-49d5-a631-fcd1fa6e24d4; loginPref=A; gfs=msegfs; al=3; XSRF-TOKEN=ef84e03a-a97b-46af-9cbb-030e2c15421e; cbinrng=Range_None; tgck=D_OPT0329_LinkSizeAndColor_TestD_July2021|A_OPT0497_Citi_BE_Award_ACQ-Oct2024_Update|BO_OPT0403_CoBrandCC_newtext_Test|BO_TripInsThrottle_new|AE_OPT0497_Citi_SMB_Award_Business_AAdvantage-Oct2024_Update|DO_OPT0329_LinkSizeAndColor_TestD_July2021|B_OPT0487_AADV_Event_test|B_OPT0483-CobrandBookingBPTakedowFS_Exp|B_OPT0403_CoBrandCC_newtext_Test|BD_TripInsThrottle_new|BO_OPT0487_AADV_Event_test|A_OPT0488_Nested_Ctrl; sessionLocale=en_US; gfsid=KQEFSC; access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6Imd6dGNwaEZMWlY3UjBqbk12SE1jeDk3LUUtSV9SUzI1NiIsInBpLmF0bSI6IjI2bmsifQ.eyJzY29wZSI6InByb2ZpbGUiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOltdLCJjbGllbnRfaWQiOiJhYWNvbSIsImlzcyI6Imh0dHBzOi8vbG9naW4uYWEuY29tL2xveWFsdHkiLCJpYXQiOjE3MjkzOTM5MzAsImNsaWVudF9rZXkiOiJFTVBUWSIsInN1YiI6IjA2Q1RKOTAiLCJleHAiOjE3MjkzOTY2MzB9.i6hF68_jfKOab1qzyg2m5VzoCyBt0hIXfGhGDBsgF6th4E1lgBjbHDa2RNRQCeEiS3OBBNdZ_f6IF_CYoiawvN3CrPmndnbgbLA8NMKik6YHLDgl0IQU9Vbc-R8xTmlNGTFm0OLEEWgXFwNkk6VXPM9VGSDnnNO03U2QcR_bBXCVmSbXhtcY3CEd_IiRJHhql0uLeJ9vgrluKz9J4wBdCKtO08su2e8YgV-3Y4nhrUYuqBEAWi9MLOfH5VGxcO_Lw0xYSMbYMEKxjpkRjjdSOX3JB0SJ3qiXrBtvc5Gdp5cGVEdOST__Q2WwN9ZXm2Q6tRLJPUxUCMsWoCJQwxaMxw; refresh_token=LndJDodvmo4FA7YMCkVk1frldeuQWCoQwBz.s9cokw; DYN_USER=ETMsDgAAAZKn6TQHABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEDTjG%2F8MRefFS%2B6LSBSiolgAAAAQTyguX%2FcNk8rV9ebXpfK1pQAUj5Sd8hIKeRfScgCzQ0nnOAc%2FZWQ%3D; mac=ETMsDgAAAZKn6TQJABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEIEXVS%2BrhoSTNe3DrEtkGLoAAAAg4x6i46o%2Bsq%2BfrF4v71Pm5VvI%2B%2FdKhhizGFOyUSucHxAAFMIE%2FJeeRDu8mOVeC9AUyZnkswFb; akavpau_www_aalogin=1729394231~id=410af41dfed578d10272c6b2109b596c; X-AK-PIM-INJECT=sync; KROUTEID=d72c26943ef1d6f636eda9398391ee0f|86b99df97e9306037645a42147508174; sessionType=unsecure; JSESSIONID=2E81C0C24504BFD0091D3597D32C3BE9; ROUTEID=IKSS.green; AKA_A2=A; akavpau_www_aahomepage=1729521653~id=9e27a62174d17b6209e4a34bc63c3460; OPTOUTMULTI_EXP=Sun, 19 Jan 2025 15:35:54 GMT; mboxEdgeCluster=34; dtCookie=v_4_srv_2_sn_02CF7533F8EF8E84742AD11FE6EE52A5_perc_100000_ol_0_mul_1_app-3A165a5cc5c5fd7c11_1_app-3A8b2a7e44ceb3fcd4_1_app-3Abd9e4e597cdc58a4_1_app-3A4aaa3de5a7188090_1_rcs-3Acss_0; AMCV_025C69945392449B0A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C20018%7CMCMID%7C21679992250229964980707030570960980556%7CMCAAMLH-1730126154%7C9%7CMCAAMB-1730126154%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1729528554s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; rxvt=1729523154857|1729521354013; dtPC=2$321354012_849h-vRADKMJTLJHRKRRTAFHKHRHFRKFQKCCUH-0e0; bm_mi=8A454007AFC1294436CFF396EA70AC96~YAAQi9XdF0TMs1qSAQAAloiBrxnqBMYJq+4HyoVdUVhlz5upuFKVcATZPrSV1fQivC6ammeQsJsmfHWrNq+fZqlbvp26dCeLt026fhvVy3Lsb26IlfzajCD9elvZV79qfxwTLqnJWkZXxpcQIzyfak+e0j3g6IvBUvzUS3OuawbnRb2wnIPBbHFRyUEgjcC+422LPZ4tYMDnqGoZikdhisTQH7IoOLg91kuNVTbz4RURBF4RceOaW7kV3w+j8G7+kjRUX5Qguf8w7oUuhrTnmMWijEwoQSmLCG1fjVe5ZjQ5EgfrEEdyPueiYgvFCW/9L4JH8s5cFQ==~1; QSI_HistorySession=https%3A%2F%2Fwww.aa.com%2Fbooking%2Ffind-flights~1729511533002%7Chttps%3A%2F%2Fwww.aa.com%2FhomePage.do~1729521355075; ak_bmsc=B1F9C05221E986EBE56FAC5CB470DF35~000000000000000000000000000000~YAAQi9XdF1LMs1qSAQAAUomBrxn/HeTqkJvtktw3brA+lAS25BvmTFFyzLhcLoq2amqGqBnQCq2D50oTQybdSXWVw6mgPsTQhYHVAtBUtvpQpVV5J+R4nZ1pjZMeM+ap/3l6HotVs4kXl1/tWnwgB0zMyTzOvDyXhFpmH9PR9GO5iK3GsNnA314ckCd3EI7FyPt0V1tNLsy8obvXTBd1Egfw5EvkBAp4PU65L+yU2Jr+Jf5qMG+jQfsiBAeHdP88FhraFaWyOpQ15rvcwMul0j4xyiu+5aJymaZDdsXpVuW+Y1Me57XbJNWio0iAGiEum2ImcwkigUgmlVWeXTrBx2RqzgwZInS4W7KeEJ2NHeWFnmz6/Ugrb354CKd5LPwJwfDJdsN+sGN10oOZSrtHwG5O/hHcOHUIXHUbMJWMFcRQ6spmItTXIMHmo1zLfPX0sFMQuadTQ+kDxCR776E2sgQ3bw7vpcSyDTddk2xt; QuantumMetricSessionID=3f09d2305f85934d0e6aa7dc80574c5f; dtSa=true%7CC%7C-1%7CSearch%7C-%7C1729521368092%7C321354012_849%7Chttps%3A%2F%2Fwww.aa.com%2FhomePage.do%7C%7C%7C%7C; RT="z=1&dm=www.aa.com&si=ae8c3eb3-317b-4010-96b6-9545f8755be0&ss=m2j4cvez&sl=1&tt=9b&rl=1"; mbox=PC#02ae0a1f35b3412a90aafd1a7c76d911.34_0#1792766175|session#b917d14d17c342b0828b65e571a572bf#1729523235; s_tp=14056; s_ppv=Choose%2520Flights%2C8%2C8%2C1088; aka_lc_code=ML; bm_sv=F2501BAEB59D889FC0522DBA04D3CED6~YAAQi9XdFwfQs1qSAQAAZ/2BrxlNaXIMtKpRZ4yVclmYL3Od8IR2D6EF+RjdcpEeAqhwPkpDMoNcX6TXBe/CcVG7GNqhwPr0PV+w0wZ28YimlRM1ObkV0z0y4VDTSdKAG5eu5o90f8LES+4tGT7xEYbp782ImmLeftFcEO7UrTp9EcukMiR1lIBO6bkk2Ct7Ay379yFHgE7LqCH8CAE0KLpJP52neUj2sIn1aMk2ZXhASe+rcSVk/60xEMmy~1; bm_sz=A0DD0EB872D08161C35268A7B384B5CE~YAAQi9XdFwjQs1qSAQAAZ/2Brxl+QldTy0kw4h8w5SNiy00j4ADmcv7s/Uo4UJDtEEKsnzyQo5jZV601rvgaHr3mjIcyVZ2UbxnCpmx/q1rFDq/3jt+bzIc2epDnkinPDuNCZYAaiv4JU3jwM47FYQ3n2gP4s6Vrd/fKHPyZgztSnYuTZ5vnG6baom0nGpzIvKDYeUEWs3Q/m8tyeOhmG6M3d0mv/HdBmBKf5VH/QqOESsl94i9WLffsGvJTeFaNZ5dO3XYzAo0Tbp/nPgpoRR9ThR3pxiL2IKO6R0criJlxlH9bvuQZkhILjek+LbAywJwNXIpWu7cCM6ONOspfZ+UOPvPNq9pCc3jP2ilFXp4AE5pn7NIzoejfPM76AGKoQ0J39YHQkd0SjVs9nNsIHpChUOUI7oPlN9jqsbbmJeiRestuZ1lqiyPeEVfp/Fhp2cPuncI4zBuXNlyy12YfCK9rvPYkPGn2Gvjzelzm1DVebCAqtpDh03j/uqR2Cqf6Jr7kje7vw/l63+QJAlo=~3290681~4277299; utag_main=v_id:0186f4e0eef70026d0171c35558805075007106d00c48$_sn:251$_ss:0$_st:1729523184821$vapi_domain:aa.com$_se:3$ses_id:1729521354090%3Bexp-session$_pn:2%3Bexp-session$eyl:5ded0dfe0eadb0b17d988d7b0f2667d0%3Bexp-session$loytir:Guest%3Bexp-session$lid:Guest%3Bexp-session$sr_tt:A%3Bexp-1729524974705; s_sq=%5B%5BB%5D%5D; akavpau_www_aafullsite=1729521688~id=16164cd038c47a03007aa4677fe59eb2; _abck=F095BA83AF15D7724DB5179B7DFA0EC9~0~YAAQi9XdF4PQs1qSAQAAowqCrwwZ6ihAvNf3SCWueICHTzd0U+PxGgb53TA4wGrOhlvtD1yTznlEHUl0tGFU07qFmJMxz34apeIce7cHHpApoCiAlK5Hu9mwjfP/EM2Y+p7fK2QJNkiinu8dedqOjmzyxYO9P9DzRIAjYmQ31aRbtm8vDP8oDCy5QtUusgt+acLT3bvSvHpm1hHeqU0w4nBO1lhRDI2rNaYv+NAjNjvsMjoOl6DK8tuoiuLnjl7YMJck/cH6W0qghj0cZT9eJpwt6RVU2Te7HQHKzTB1icWAj/L3nVCVTVDIcWI/qvt2+CKwQYkylb17Uo7KbsrhTK0wAZL05rwtfgTkKvvGUIV/7OczeIUYu+/orp+ac6yvATmtSmwvvjF2hD0/CloAREcgn6YdVzbQqMGFhWwPFx16lMszlrDWBc3KBYr48GiSaL8XlZLWwxZSTXEp3RJ+Hw+AJMX3bFp6TM1OmcwCRaYTRtq51fQYOUjCMRURIqW1YsfqCsQDxfPtUKs5itF6utK//4/V59FLnwz+kyHCIJwHwqF/8SZBn3lTOmu+ESBKcOcIgVG3xrCGyxebeFJ/zXpTqKyp66KwdLOlmKt9vIvkQYokETGWJR65NzBw5nt+WAL91jHj3rr1TWTLx83T70GwAGJNFd0tGSbHA28bK+VUr2M197FsVgoh20JE3p1VqBqhTeHaSdIjP1n0yE8eV+N+OVYwti2fc0pm2kzJf7qsFRBSUBIwLdRQ3odjZhDgCfJDrK1XQkhAhDl0+VqqA7GaDaVBhYpu7GfZJWcVl02zOtKVIU2E~-1~||0||~1729523976; _abck=F095BA83AF15D7724DB5179B7DFA0EC9~-1~YAAQjB3fF24k3q2SAQAA9FiErwxId9HJSYUqsMclxUA/RoraevJJA+Fwc5KGOkwDDvktn2Y7U7wHtgS7z01gPI8r3Oh5cscfrOwHjG+uEQlflOdUczZEMdNyj7PbH4R5ENJ3G1G8cHtws5NWuV1myjIFVJGHUKe4sUnb5OtS6EXYA+UDjap96XwaRN4FvJ4XjmGE3lmr8RuQ8fBivRd0FlHeR19Jnc/VBQE8d5H2hS44hjOKRYTImXB2LT27FtFhgy7t9tbGnpzYvbeN5GGRKIiMjOQPon1UXjc0wBXEZwZV3fS7FoGNCBHb32u8GLfNkmFwP06XLQlOFnZlMYU1NYytZM2f0DnwXVRR7sAjO1OmRWhBmSYGXMUX7uSdzXX9d6r0LD5SP9pvrAux1+OVOeWczczihWgtbGwHfgpnylHt7pw3IYxZvD5+gQjJbPNKLpj6PaByCdBXdSOPGt4D1e64lyr3+bTGF4LyfkiDmQvHBb7anN6CI8gpVybqfXB3hYLMJsNTvf3kBr/lhOGgnSM2PCpn3tv8lALRLwr+3XJeP4XsY1XdLHjMUjsZVEUtKHsJSIXZXLTUhYlJNtdUDafirNRq7Jw9bIs/+yE2jYUwA3ZjN3HIC8pEIV8nzHez+m2hTR8TURQ/+A3dYN+t7kbB+Y+R5xYUEoFN/IbbitNsfq1OEzL06cIxo4K6WMW84XI3khUkTZN94syGnRdBf90fTZIW+YIguf7kEKUdVw==~0~-1~1729523976; bm_sv=F2501BAEB59D889FC0522DBA04D3CED6~YAAQjB3fF3Ak3q2SAQAA9FiErxl49JzYy07uaqvEIYwhFS2o6xvxKl026hBRTkkpAsBictVz7tx+kbhy0iJPzg9Hnm8zoHx82f34vhrDznQV8XJFhTiCT9RWghq3XEoumc2weszBwuTgugndZ7/XKm95GmPJU1zKXHkKVXpez8rs0Dy3R6MoHxol5cYL64SDyjWoa0c1gEvaLMG+p1JcPYujf4PHVWAiqhsoSF34emXy/POcawthQhASc6jw~1; bm_sz=A0DD0EB872D08161C35268A7B384B5CE~YAAQjB3fF3Ek3q2SAQAA9FiErxkjS/f/o6dk3P5qe1h/AIvWuOw7D4zQoRYl2hvScEu8jlFUPPpTpkmCg1vVRDOL6xnpiN6R7GKRlUH60IB0NxIdeuPToei0DARGn82rwiqfa/8oVb3VVuqZSEVJVC8oGqgIWU7MML9dxEg3kP/1nmwUZapFO8mrlCPLlIQaBHgR+DAUpqabgXYy4KVzzNzJ5lTBMv2YJPukCWYG33LLJ7hmb9felTe2CymDztVq0+dLsySWXnbMPn55NaODr1PhOjF3ucyCpMWmmRGhK/st+ERfxOOqq4DhtVti61/DtUQpxotz+QLTsEJNjrSMLV3sdQkJBnmk/S54n0JjbJHZADoAP8T6fGKadZCJByuGD4m/EFxq0oIvdhJ9CCQUO1ugY/u3ezz1qvp0DANJPrQwBn1ct131TX/Dv0cRAQiZrFP9jmDLLx86vsRIX2ZArAA7lT8mr6CQT5rhR9yp82O5cNPW/8VQvDRAmWWB/me3WAoRm3J57fHJADfevFowGw==~3290681~4277299; aka_lc_code=ML; akavpau_www_aafullsite=1729521839~id=d11941766646910392478809875680d2',
  'origin': 'https://www.aa.com',
  'priority': 'u=1, i',
  'referer': 'https://www.aa.com/booking/choose-flights/1?sid=4083ad5f-f741-4c29-ac1a-322c80a80958',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
  'x-cid': '9383dd35-2587-49d5-a631-fcd1fa6e24d4',
  'x-xsrf-token': 'ef84e03a-a97b-46af-9cbb-030e2c15421e'
}
conn.request("POST", "/booking/api/search/calendar", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))