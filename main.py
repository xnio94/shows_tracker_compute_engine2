# Copyright 2019 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import time

from code.download import get_video
from code.selinuim import start_driver, scroll_to_end, get_last_episode_data
from code.globals import minute, batch_duration

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET'])
# def say_hello():
#     driver = start_driver(headless=True)
#     show = "https://www.snapchat.com/p/f4814d0b-4f59-45e1-9d32-8f705f6544db/2407097341865984"
#     driver.get(show)
#     scroll_to_end(driver)
#     episode_link, title, poster, time_posted = get_last_episode_data(driver, minute=minute)
#
#
#     data = {
#         "episode_link":episode_link,
#         "title":title,
#         "poster":poster,
#         "time_posted":time_posted,
#     }
#
#     data = json.dumps(data)
#
#     return "Hello, world!" + str(data)
#
#
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True)
from code.send_email import send_email
from code.transcriber import transcribe_audio

driver = start_driver(headless=True)
show = "https://www.snapchat.com/p/f4814d0b-4f59-45e1-9d32-8f705f6544db/2407097341865984"


#
# def process(episode_link, title, poster):
#     print(f"processing episode : {episode_link}")
#     video_url, audio_url = get_video(episode_link)
#     transcript = transcribe_audio(audio_url)
#     send_email(episode_link, transcript, title, poster)
#     # send_email(text, title, poster)
#
# shows = [
#     "https://www.snapchat.com/p/f4814d0b-4f59-45e1-9d32-8f705f6544db/2407097341865984",
#     "https://story.snapchat.com/p/7fb3463b-7ec8-47a1-8a99-18577e7f8231",
#     "https://www.snapchat.com/p/8b8ceb94-9e29-4ec0-b1de-33753754c969/2548940717385728",
#     "https://www.snapchat.com/p/86dba8a2-357c-4f69-8da4-0dd6b9d1c733/2556652314200064",
#     "https://www.snapchat.com/p/e6dd5e6d-e78f-418e-acb9-7ae390cfcc29/760047972395008",
#     "https://story.snapchat.com/p/9435544a-2473-4fde-a379-e34da381dc73",
#     "https://story.snapchat.com/p/71c666da-d7ba-41f0-8c53-dab6348bf9f6",
#     "https://story.snapchat.com/p/e3c883e5-c9cf-4322-858b-785dcfa6d824",
#     "https://story.snapchat.com/p/e3b64bf3-709d-46e6-82bb-f4f901e311e8",
#     "https://www.snapchat.com/p/e6492ed0-1aec-42d6-a765-3eb9011decb4",
#     "https://story.snapchat.com/p/3b16948a-97ac-4c52-a546-263de3a33b56",
#     "https://www.snapchat.com/p/0d9559c7-2cff-4a45-9293-b46c64df3b25/1436225626333184",
#     "https://www.snapchat.com/p/7da4a6d1-c124-4ab0-a00f-d0c7986b2c9c/2556657579313152",
#     "https://www.snapchat.com/p/ca4af9b0-1ec5-42b3-acd1-9775f0b0f8fd/760057326614528",
#     "https://www.snapchat.com/p/139305d0-62fd-4e70-aca1-04e6b35e40e3/2407087524593664",
#     "https://story.snapchat.com/p/7de29ce9-ca30-4867-a021-31e2109655f8/1436230316457984",
#     "https://www.snapchat.com/p/31355a0d-da7a-4bcb-8ad1-fbf4775b3104/2556659483140096",
#     "https://story.snapchat.com/p/fef98314-225d-4718-acb7-16fff1e10576/917270960945152",
# ]
# # def get_video(link): take episode link and return download link
#
# current_batch = []
# for i in range(4):
#     send_email("episode_link", "transcript", "title", "poster")
#
#     last_batch = current_batch
#     current_batch = []
#     for show in shows[-5:]:
#         driver.get(show)
#         scroll_to_end(driver)
#         episode_link, title, poster, time_posted = get_last_episode_data(driver, minute=minute)
#         print(title, "\n", time_posted)
#         if episode_link != '' :
#             if episode_link not in (current_batch + last_batch):
#                 current_batch.append(episode_link)
#                 process(episode_link, title, poster)
#         print("################")
#     #
#     # time.sleep(batch_duration*60)
#






while(True):

    driver.get(show)
    scroll_to_end(driver)
    episode_link, title, poster, time_posted = get_last_episode_data(driver, minute=minute)


    data = {
        "episode_link":episode_link,
        "title":title,
        "poster":poster,
        "time_posted":time_posted,
    }

    data = json.dumps(data)

    print(data)
    time.sleep(1)

    send_email(episode_link, "transcript"+ str(time_posted), title, poster)
