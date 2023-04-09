import os

class Config(object):
    API_ID = int(os.environ.get("22697940"))
    API_HASH = os.environ.get("02f7a14ec44595dcfbbbab4d0ca06f46")
    BOT_TOKEN = os.environ.get("6039692420:AAHXs5xMCAavHDERE-hSsk2mDdKTv73uDKw")
    STRING_SESSION = os.environ.get("BQADyZKZnUmFJ9y0JyKldNn4-Z9YJZfeJFXeo1MIO7NWR2OE0t6IziKpf_FKT745aYVX7uE6KE61d76bbFEoeEh0eKkmFwOgFke_ijLwPQ4KOMFw_h0a4uHvC3Z99kbkU4qLDNzCjWYKZkCzN6ksibRytVOvO0VVFat_KkFmfYE6fitctUugn7SQZEVt8_feT6_jQMVF_lp-WwTtKIVib-ccGgdaGqcrmYuUCZMIDNqjSkeqtaT5f39DCN1T0aAa5WQ2q2xyKsqkvaM2o65jbkipvbkK3UFLH44F40j3ekhoYRPNL_mXfU0ce3tYQ-VIaRdXJYQjWBx4RjVIu93WFBnJAAAAAVy9ArMA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("@angryarmy_bot")
    
    START_IMG = os.environ.get("START_IMG", "")
    CMD_IMG = os.environ.get("CMD_IMG", "https://t.me/Angry_army/107")
    ASSISTANT_ID = int(os.environ.get("5850858163")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
