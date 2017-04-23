import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
	username='6187df37-acb7-4f66-8606-0c448981617c',
	password='jM5lIli5vJqz',
	version='2017-04-23')

workspace_id = '38507657-c0eb-43eb-a77d-9083bdb20bc5'

def get_node(response):
	return response['output']['nodes_visited'][0]

def get_response():
	user_input = input(">>>")
	return conversation.message(workspace_id=workspace_id, message_input={'text':user_input})

def get_root():
	return conversation.message(workspace_id=workspace_id, message_input={'text':'root'})

def print_text(response):
	for message in response['output']['text']:
		print(message)


def domestic_abuse():
	while True:
		response = get_root()
		print_text(response)      #prints Watson's response
		response = get_response()  #gets input
		if get_node(response) == 'DOMESTIC':  #if input text is Domestic
			print_text(response)  #prints Watson's initial reponse
			while True:
				yes_or_no = get_response()   #gets input of yes or no
				if get_node(yes_or_no) == 'NO':
					print_text(yes_or_no)   #Watson responding with what he got (no)
					while True:
						no_response = get_root()
						print_text(no_response)
						break
				elif get_node(yes_or_no) == 'YES':
					print_text(yes_or_no)
					while True:
						yes_response = get_response()
						print_text(yes_response)
						break

while True:
	response = get_root()
	print_text(response)
	response = get_response()
	if get_node(response) == 'HEALTH':
		print_text(response)
		while True:
			yes_or_no = get_response()
			if get_node(yes_or_no) == 'NO':
				print_text(yes_or_no)
				break
			elif get_node(yes_or_no) == 'YES':
				print_text(yes_or_no)
				break
