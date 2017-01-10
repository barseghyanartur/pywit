import sys
from wit import Wit


def send(request, response):
    print(response['text'])

actions = {
    'send': send,
}


if __name__ == '__main__':
	if len(sys.argv) != 2:
	    print('usage: python ' + sys.argv[0] + ' <wit-token>')
	    exit(1)
	else:
		access_token = sys.argv[1]
		client = Wit(access_token=access_token, actions=actions)
		client.interactive()
