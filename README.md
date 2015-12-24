## cli-yandex-translate
## 1. Command line utility for translate words and texts using Yandex Translate API.
## 2. Command line utility for random showing words from local .csv dictionary. For example, you can synchronise this file using cloud services (Dropbox, Yandex.Disk, etc.).

### 1. How to setup
1. You are need Python (I'm using 3.4 version, but I think version doesn't have matter).
1. Download ya-translate.py to own dir, in my case *~/projects/own/samples/python/english-words/*.
2. Get free Yandex Translate API key [here](https://tech.yandex.com/translate/). You also can see language list on this site.
3. Add this key to your environment variable (YANDEX_TRANSLATE_KEY).
4. Create .csv-file for your own dictionary, for example
```sh
touch ~/soft/dict/yandex-translate-dictionary.csv
```  
#### Todo-list (change dir and languages to yours):
```sh
echo "alias trans='python3.4 ~/projects/own/github/cli-yandex-translate/ya-translate.py en-ru'" >> ~/.bashrc
echo "alias transr='python3.4 ~/projects/own/github/cli-yandex-translate/ya-translate.py ru-en'" >> ~/.bashrc
echo "export YANDEX_TRANSLATE_KEY=your_own_long_YA_translate_key_from_site" >> ~/.bashrc
echo "export YANDEX_TRANSLATE_DICTIONARY_FILE=~/soft/dict/yandex-translate-dictionary.csv" >> ~/.bashrc
source ~/.bashrc
```

#### Using from command line:
```trans hello```  
```transr привет```  
```trans 'hello my dear friend'```  
```transr 'привет, мой дорогой друг'```  
```trans 'hello my dear friend' -a```  

### 2. How to setup
#### Todo-list (change dir and languages to yours):  
```sh
echo "alias nword='python3.4 ~/projects/own/github/cli-yandex-translate/english-words.py'" >> ~/.bashrc
echo "alias clear='clear; nword'" >> ~/.bashrc
source ~/.bashrc
```

#### Using from command line:
```clear```