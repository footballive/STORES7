from email import message
import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=
[]):
  message_cetainty = 0
has_required_words = True

for word in user_message:
    if word in recognised_words:
        message_certainty=1

     percentage = float(message_certainty) / float(len(recognised_words))  

     for word in required_words:
         if word not in user_message:
             has_required_words = False
             break

            if has_required_words or single_response:
                return int(percentage*100) 
                else:
                    return 0

def get_response(user_input):
  split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
  response = check_all_messages(split_message)
  return response

while True:
    print('Bot:  ' + get_response(input('you:  ')))