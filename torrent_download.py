from qbittorrent import Client

qb = Client('http://127.0.0.1:8080/')

qb.login('vayer', 'vayertorrent')
# not required when 'Bypass from localhost' setting is active.
# defaults to admin:admin.
# to use defaults, just do qb.login()

torrents = qb.torrents()

for torrent in torrents:
    print (torrent['name'])
magnet_link = "https://zamunda.net/magnetlink/download_go.php?id=590279&m=x"
qb.download_from_link(magnet_link)
