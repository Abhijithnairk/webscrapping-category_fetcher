import requests
import pandas as pd


competitor_list = [
    {
        'url':"https://shop.thefreshmarket.com/api/v2/store_products?limit=60&search_term=",
        'cookie':"osano_consentmanager_uuid=307c376c-f10d-4107-a573-c7e1f10af7f3; osano_consentmanager=3x8MgIHnK_nVJk5KmuOnd2sHDJYR8FP6k1pCkCaxdqC0pkZknRQR80VRjB6Kbgp7iGjMUnsPLnme8DWmUxRLBTj48Z3TkM1LJINdRgM__wpe-q8XngljF-JbFVnkfXq4LfhXRd5iPf89ikmPWXa635YOVLE924Ot8lU-D_E4Xy6P1mJcughXVg5oPt56dUVNqJH39oco4BAJ-E9jqf6qFimUuhbedA890lkIoINBn4wilHtXcqRTKzrDKkkaBU4EXcSmTg2iAG1Ry3jlpaURHTclVU9KceLsUfw0QQ==; _gcl_au=1.1.1454964145.1706631619; _gid=GA1.2.921200125.1706631621; _fbp=fb.1.1706631621548.1772768121; _pin_unauth=dWlkPU5qZzVOR1ZsTlRVdFl6SmtZeTAwWmpNekxUazBaVGd0TURoa01EWmxabVF4TkRNMg; ajs_anonymous_id=d6854b93-7b07-407f-a94f-839dc66712ed; __stripe_mid=6a035359-a082-4788-a444-cbc813a5b8ab5862e9; fw_se={%22value%22:%22fws2.904b7ea3-3c52-4b73-982f-fe0d1a5c7217.3.1706678484364%22%2C%22createTime%22:%222024-01-31T05:21:24.364Z%22}; _uetsid=76a87b70bf8b11eeb2461f63bc1d7a0c; _uetvid=76a8e760bf8b11ee8e7067f8c6f9fc7b; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-01-31T05:22:41.980Z%22}; _ga_EMDXDP2N4W=GS1.2.1706678486.2.1.1706678564.44.0.0; __stripe_sid=4de0f57b-def4-4649-9359-d819c0aac2c083aadd; __cf_bm=yKgtT0SxPcrWLh9iLS4z.5LN74Bl9gGS1bQ5nIlm1ws-1706679642-1-AQnN0qxyxZkNsf4EPffEx3ZkrpN7ENQJY2c8Qjwrw0X6fvsHxqE/74zELvOt4w5Uu5QgZKDHPi0k7f6cNWRKCUA=; session-prd-tfm=.eJxNic2OgjAYAN-lZ2MoWn-4bRTYNlJCFmTphQAW_VBAKaxSs---HPcwmWTmjdKyk-qCrDK7KTlD6V12ddbIpkdW3w1TUVIpaJu0b6-yQRaSI7vkbgE-MBppijmw7XyKuDCP44QuzNtPftvexY6uaFUsRWUbSegZh_BK_LDoucsgAQxJ5dSHONA89ha8nry3lwKoos1Ri29WZnEAfhWNXEcm197ysGMX4eJ7_v_XBOfuU9HaGXKTkDze4mKkq9Mnw-LrCVnsGLRqX1x_mLzyXn5o4zKYZxs_OLfQqeZJyt3eJqPI-qhU6WN9TgY4JnYPxoMzx1VohgYluxROyCLmmqzWi83vHyX9aTc.GJtu-A.RJLQ3Mfh0E7W1nhZBpran31K4Yg; _gat_UA-000000000-1=1; _dd_s=rum=0&expire=1706680572827; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-01-31T05:41:13.278Z%22}; fw_uid={%22value%22:%2226a02601-620e-4807-af18-cc8bd1ab86fd%22%2C%22createTime%22:%222024-01-31T05:41:13.294Z%22}; _ga=GA1.1.1783481186.1706631620; _ga_2NZ40CS25B=GS1.1.1706678485.4.1.1706679673.57.0.0"

    },
    {
        'url':"https://shop.wegmans.com/api/v2/store_products?limit=60&search_term=",
        'cookie':"AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY3NDMzMDE5Mjg2MzkwNzA4NDMxMjQwNjIzODI4ODk4OTU0NDg3NlIRCOjK_qfXMRgBKgRJTkQxMAPwAejK_qfXMQ==; _fbp=fb.1.1707064928542.970134091; _pin_unauth=dWlkPU1EWmhNVFkwWkdNdFpXVmhOaTAwTkRsaUxUaGxOREF0Tm1ReFpXUm1NekpoWmpZMw; wfmStoreId=16; _gcl_au=1.1.1317534410.1707064931; wfm.tracking.sessionStart=1707064930868; at_check=true; ajs_anonymous_id=059f6a11-ae22-4f6f-b39d-7f6b556e796e; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19758%7CMCMID%7C74330192863907084312406238288989544876%7CMCAAMLH-1707669734%7C12%7CMCAAMB-1707669734%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1707072134s%7CNONE%7CMCSYNCSOP%7C411-19765%7CMCCIDH%7C0%7CvVersion%7C5.5.0; inRedirectGoldPanAudience=1; dotcomSearchId=0176c351-a45d-4fd6-abf5-abaee76e2db1; wfm.tracking.x2p=1; sa-user-id=s%253A0-f390e651-f60a-41f4-6020-3f2766c03add.egatitxhFKly5yawcH3YQuWCe9w8zo%252F509etSbCtR%252BY; sa-user-id-v2=s%253A85DmUfYKQfRgID8nZsA63Q.RJzE1DcMzzJmU7yLvExinlYq708BKumcbGIwP2gQtZI; sa-user-id-v3=s%253AAQAKIKYBAcJ4EkAuLW2Fc6yZOj_aZeW8YO7-GkqhWHvcrZLbENQHGAIg4Pz-rQY6BITuPeRCBC6MWV4.ZLGn13FPF4Hhr6q5XYHr84Ir%252Bjprwz9Ko8kFywbL9ao; _pin_unauth=dWlkPU1EWmhNVFkwWkdNdFpXVmhOaTAwTkRsaUxUaGxOREF0Tm1ReFpXUm1NekpoWmpZMw; at_check=true; ajs_anonymous_id=059f6a11-ae22-4f6f-b39d-7f6b556e796e; __stripe_mid=38b2cc9a-31ec-440f-8745-6bc7f755c9f820cff4; __cf_bm=PIlBFrXWqCc78oq3uKyVM6MzWUYM65x8PNHtGX6EXWo-1707068051-1-ASZUyKbxy+61c7p+DMFnPcHAZwGdkgFO8JpEfZ2E6q5aBQEaBzeqfmKXsiIU1AADK0TjgVOlgTNwmep/X1MS+L0=; lux_uid=170706805318583133; _uetsid=591e8380c37c11ee8861f1cf4648418c; _uetvid=591eab70c37c11ee8d9db790eb9c36ae; session-prd-weg=.eJwdzkFzQ0AAhuH_suc0w05kws2QZlbtKiXExQiLZVcylgqd_veaHr7Lc_neH5BVA5UNMKqcS7oD2ZMOIu9pPwJjHKZNJJWSPfpsfHS0Bwagi9PcLwXzmIOiFamEOfp-Q7WA12XbWkD-fef6M7XQEQmHp5d3Qeyz5oY-TMVtJHb9IkxtbmG9WSnSkDR4jWDanhfMkET9dU0Tp8pjn3mtr2I7epHWhNia2S0OxjzW_r8SyDvUPqcyfknX2qKEPtFY_S4TzLw-WMo4kkjwptw6cFjMZDUhsbvFS5S9PrNKdFh31QCbHvn6sD5NMb650aHuHicUnYLJz-5uyOca7MAk6ZCxEhgHTdHUo3JUfv8AddxqEg.GKFcFQ.CAwXLxl9tVuXbtcDaP3iE868S04; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; mbox=PC#071fe51bfe4140ae836fff529c9660d5.41_0#1770309770|session#de0356ac40684463aa4c4f157ab6de94#1707069917; _dd_s=rum=0&expire=1707068954869"

    },
    {
         'url':"https://shop.sprouts.com/api/v2/store_products?limit=60&search_term=",
         'cookie':"_gcl_au=1.1.864550040.1707064713; __cf_bm=acR0UI5uDoZnEYZ_TNB..zyXFEVlK.zutm6UTTgRvVo-1707064724-1-Aewhicw8ldqjzOEnxNBAw8jSkQr+6D8JfKY+YB/1mGhDIWacZlDrMaFH4VveddRpDEjN/mRvcEqHGGwr0sQ6DTQ=; _gid=GA1.2.2022142842.1707064725; BVBRANDID=3bde11bf-12d1-4989-b8bb-563ca740f795; BVBRANDSID=4e6604f0-fee6-4298-b616-cfa932c57771; _fbp=fb.1.1707064725870.629512548; loyaltyID=undefined; _pin_unauth=dWlkPU1EWmhNVFkwWkdNdFpXVmhOaTAwTkRsaUxUaGxOREF0Tm1ReFpXUm1NekpoWmpZMw; ajs_anonymous_id=f0004c7e-f8bb-4912-b63e-787c40b55692; dotcomSearchId=55be17ee-c436-4339-837d-651b48b32715; ajs_anonymous_id=f0004c7e-f8bb-4912-b63e-787c40b55692; _pin_unauth=dWlkPU1EWmhNVFkwWkdNdFpXVmhOaTAwTkRsaUxUaGxOREF0Tm1ReFpXUm1NekpoWmpZMw; __stripe_mid=832196f2-b973-4164-b2bf-a5302a94fa17622ba8; __stripe_sid=f08a768e-ffd2-4d40-88fc-9fac6a899ca2d9612c; session-sprouts=.eJwdjsuOgjAARf-la2OggiPsCDimxBZxUB6bBqGGIlZDiwgT_32ayc3dnM05v4BeeyYb4F7LTrIFoE_W30vBhAKu6gdNJJOSPwRVjxsTwAVsCpvLruIRD9FpRibhobPU0KzgedKfK9i9Lp3zLHy0Rq1n5y3R2877NLZyiBUJchv7hk0SrNl2xPC7yZPbKtrFJvaRROI8F1l4LdOYRy0yosCDUZCP2B95nh5Vmdr_rgx2N9Q-hzp9y72vo-7OwFLzVWeYR-I41elJonvX1LoDJ9VIZg-SoJrIyljy7EEZLa3k51A4-F1nkSLxYFLi09ckLHV6f3lhYY0HvAULMEjWU14DF1obY71ZG8bnD3-laO0.GKFPWQ.CQC_IfM17KqqGurIkUfpDQW_rT0; _ga_LPZ816BHL5=GS1.1.1707064724.1.1.1707064794.57.0.0; _ga=GA1.2.1383161882.1707064725; _gat_UA-47434162-1=1; _uetsid=dca53b00c37b11ee88ea257066808dbd; _uetvid=dca5a230c37b11ee9a9991b0ec599883; _dd_s=rum=0&expire=1707065694626"

    },

]   

searchterm='Apple'
cookie=competitor_list[0]['cookie']


HEADERS={

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie  
}
URL=competitor_list[0]["url"]+"apple"
responses=requests.get(URL,headers=HEADERS)
data=responses.json()
items=data.get('items')

for item in items:
        if (searchterm in item.get('name')):
            print(item.get('name'))
            
            
print("--------filtered data below-----------")

for item in items:
    for category in item.get('categories'):
        if(category.get('name')=='Fresh Fruits'):
            if(searchterm in item.get('name')):
                print(item.get('name'))
