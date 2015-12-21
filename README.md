# cli-yandex-translate
Command line utility for translate words and texts using Yandex Translate API

## How to setup
1. You are need Python (I'm using 3.4 version, but I think version doesn't have matter).
1. Download ya-translate.py to own dir, in my case *~/projects/own/samples/python/english-words/*.
2. Get free Yandex Translate API key [here](https://tech.yandex.com/translate/). You also can see language list on this site.
3. Add this key to your environment variable (YANDEX_TRANSLATE_KEY), and use it.
Todo-list (change dir and languages to yours):
```sh
echo "alias trans='python3.4 ~/projects/own/samples/python/english-words/ya-translate.py en-ru'" >> test
echo "alias transr='python3.4 ~/projects/own/samples/python/english-words/ya-translate.py ru-en'" >> test
echo "export YANDEX_TRANSLATE_KEY=your_own_long_YA_translate_key_from_site" >> test
source ~/.bashrc
```

## Using from command line:
```trans hello```  
```transr привет```  
```trans 'hello my dear friend'```  
```transr 'привет, мой дорогой друг'```  