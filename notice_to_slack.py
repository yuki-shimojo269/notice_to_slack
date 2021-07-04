from slack_sdk import WebClient

class slack_to_Notice:
    def __init__(self,token_file_path):
        self.token_file_path = token_file_path
        self.text = 'finish learning !!'
        self.token , self.channel_name = self.get_token_channelID()
        self.client = WebClient(token=self.token)

    def get_token_channelID(self):
        with open(self.token_file_path, "r") as f:
            data=f.readlines()
        token = data[0].replace('\n','')
        channel_id = data[1].replace('\n','')
        return token,channel_id

    def send_messege(self):
        self.client.chat_postMessage(
                channel=self.channel_name,
                text = self.text
                )

def main():
    token_path = 'token.ini'
    notice = slack_to_Notice(token_path)
    try:
        notice.send_messege()
    except Exception as e:
        print(e)

if __name__=='__main__':
    main()
