import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate('0.json')  # replace with your service account key path
firebase_admin.initialize_app(cred)
db = firestore.client()

shows = [
    "https://www.snapchat.com/p/f4814d0b-4f59-45e1-9d32-8f705f6544db/2407097341865984",
    "https://www.snapchat.com/p/8b8ceb94-9e29-4ec0-b1de-33753754c969/2548940717385728",
    "https://www.snapchat.com/p/86dba8a2-357c-4f69-8da4-0dd6b9d1c733/2556652314200064",
    "https://www.snapchat.com/p/e6dd5e6d-e78f-418e-acb9-7ae390cfcc29/760047972395008",
    "https://story.snapchat.com/p/7a32ed06-5b61-4d9c-b237-0dba8e4705c6",
    "https://story.snapchat.com/p/9435544a-2473-4fde-a379-e34da381dc73",
    "https://story.snapchat.com/p/4db0cfa2-4870-4a08-8046-01acdbe26b43",
    "https://story.snapchat.com/p/71c666da-d7ba-41f0-8c53-dab6348bf9f6",
    "https://story.snapchat.com/p/e3c883e5-c9cf-4322-858b-785dcfa6d824",
    "https://story.snapchat.com/p/e3b64bf3-709d-46e6-82bb-f4f901e311e8",
    "https://www.snapchat.com/p/e6492ed0-1aec-42d6-a765-3eb9011decb4",
    "https://story.snapchat.com/p/3b16948a-97ac-4c52-a546-263de3a33b56",
    "https://story.snapchat.com/p/7fb3463b-7ec8-47a1-8a99-18577e7f8231",
    "https://www.snapchat.com/p/0d9559c7-2cff-4a45-9293-b46c64df3b25/1436225626333184",
    "https://www.snapchat.com/p/7da4a6d1-c124-4ab0-a00f-d0c7986b2c9c/2556657579313152",
    "https://www.snapchat.com/p/ca4af9b0-1ec5-42b3-acd1-9775f0b0f8fd/760057326614528",
    "https://www.snapchat.com/p/139305d0-62fd-4e70-aca1-04e6b35e40e3/2407087524593664",
    "https://story.snapchat.com/p/7de29ce9-ca30-4867-a021-31e2109655f8/1436230316457984",
    "https://www.snapchat.com/p/31355a0d-da7a-4bcb-8ad1-fbf4775b3104/2556659483140096",
    "https://story.snapchat.com/p/fef98314-225d-4718-acb7-16fff1e10576/917270960945152",
]
shows2 = [
    "https://www.snapchat.com/p/5fc3f5bf-e586-4906-b091-081a261da732/2556662176593920",
    "https://www.snapchat.com/p/7386cb35-c711-44fb-8670-fb52a4cab67c/3103101676752896",
    "https://www.snapchat.com/p/f07ee9de-a258-4b90-803f-05dc12d70a78/3225152276023296",
    "https://www.snapchat.com/p/2f4d92fa-1000-48e4-a7aa-2e09eda7f3a7/3225154943668224",
    "https://www.snapchat.com/p/4a547098-67d5-4047-a2d8-79c3a3a3a09a/917271697287168",
    "https://www.snapchat.com/p/89724162-69dc-4be0-9154-37da8923a23b/1866120596887552",
    "https://www.snapchat.com/p/9c5129cd-eae2-4baa-8cbb-4851de49a254/1015083495878656",
    "https://www.snapchat.com/p/93f44d97-3b93-466d-8844-6acf6a371420/1092088987723776",
    "https://www.snapchat.com/p/da8cd39e-c3fd-48be-a240-0e7f97c78369/827096581345280",
    "https://www.snapchat.com/p/a1694ccd-8c5c-4a72-bdbf-14c246170c03/2407097344643072",
    "https://www.snapchat.com/p/52dbf0f7-7659-4f3d-ae75-62a1decaaa2d/1866152405473280",
    "https://www.snapchat.com/p/bbf65c7c-f478-4b3a-974a-801f4d62715c/1866139690620928",
    "https://www.snapchat.com/p/58acf6d1-82ca-4952-a28c-2b25becede55/1534118352125952",
    "https://www.snapchat.com/p/aacfa589-f616-4520-aac7-0e2db2a5b7b9/760056985645056",
    "https://www.snapchat.com/p/823cc494-7a5a-405e-9cc9-c969eda6e163/760042068041728",
    "https://www.snapchat.com/p/a12c8049-ba57-48b2-9420-603095ed2245/760062204549120",
    "https://www.snapchat.com/p/c818ce26-bbf7-4e00-97e3-436b9abccc6e/760061857390592",
    "https://www.snapchat.com/p/57a69b91-b097-4c80-93b0-dddbfe48fa2f/2548928236093440",
    "https://www.snapchat.com/p/7b7f8ef9-703c-42a6-ae4c-e712dce9c3c1/2407093390317568",
    "https://www.snapchat.com/p/be3be7cb-11e1-4f84-9630-81029fb8d244/2619284429029376",
    "https://www.snapchat.com/p/59d7f9bf-e727-4faf-8de9-293a4cb02589/1534101733902336",
    "https://www.snapchat.com/p/920817d8-3073-4987-852a-49b83720444c/760039162234880",
    "https://www.snapchat.com/p/415cbcc8-599b-40c0-843d-bd1d1e3fb857/1534118226694144",
    "https://www.snapchat.com/p/f8242ba6-6e4f-4f1e-ac09-275bc1957a90/1534112282501120",
    "https://www.snapchat.com/p/c56ea3c1-e07a-43ae-b701-fadce181d25f/1534114730147840",
    "https://www.snapchat.com/p/534424af-9136-462d-9ef6-c09e6fe0ac45/760062008012800",
    "https://www.snapchat.com/p/52dbf0f7-7659-4f3d-ae75-62a1decaaa2d/1866152405473280",
]
shows = set(shows+shows2)


# Reference to your Firestore document
doc_ref = db.collection('shows').document('shows')  # replace with your collection name and document ID

# Fetch the document
doc = doc_ref.set({"shows": shows})
