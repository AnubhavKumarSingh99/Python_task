import requests
import json


#POST_API_URL
POST_URL = "https://my-json-server.typicode.com/typicode/demo/posts"

#COMMENT_API_URL
COMMENT_URL = "https://my-json-server.typicode.com/typicode/demo/comments"



posts = requests.get(POST_URL)

comments = requests.get(COMMENT_URL)



if(posts.status_code == 200 and comments.status_code == 200):
	posts = posts.json()
	comments = comments.json()
	for i in posts:
		a_list = []
		for j in comments:
			if i['id'] == j['postId']:
				a_list.append(j)
		
		if len(a_list) > 0:
			posts[i['id']-1]['comments'] = a_list
	print(json.dumps(posts))
else:
	resp = {
		"status": 404,
		"msg": "Data not found"
	}
	print(json.dumps(resp))