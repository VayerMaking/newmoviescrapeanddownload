# New Movies Scrape And Download



Using Python and Bash to automatically download the newest movies.



## First ofc

    git clone https://github.com/VayerMaking/newmoviesscrapeanddownload


## How to use

```sh
main.py
```
contains the main python script

```sh
torrent_send.sh
```
contains a bash script that is called by the main python script and it is used to transfer the torrent files download by the program to the qbittorrent folder on the raspberry pi for 24/7 automatic download

```sh
cofig_sample.sh
```

contains a sample file to store secret variables used in torrent_send.sh

```sh
cofig_sample.py
```

contains a sample file to store secret variables used in main.py

## Author

Martin Vayer - [VayerMaking](https://github.com/VayerMaking)
