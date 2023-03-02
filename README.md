# SpaceWarpDocs
 
 ## Getting Started

 `pip install -r requirements.txt`
 
 `sphinx-autobuild source/ build/html/`
 
 [Live Docs](https://spacewarpdocs.readthedocs.io/)

---
## Translations

### How to translate
1. Pick an existing language to translate from. (English is the default language)
2. Make a folder called `source-<language code>` (exp. `source-ru` for Russian)
3. Copy from the folder of the language you want to translate from.
exp.
`cp -r source/. source-ru/`
4. Now the best part! Translate the files! (You can use Google Translate or something if you want, just make sure to proof check it)
5. Once your done translating. Now come some very specific git commands to upload it correctly. 

Please not that the following commands are destrucive to the repo, so make sure you have a backup of the repo before you do this. If you have a better way to upload the contents of the language folder to a specific branch, please let me know.

6. `git branch ru`

    `git checkout ru`

    `git rm -r *; git reset -- .\source-ru`

    `git add -A`

    `git commit -m "Translated to Russian"`

    `git subtree push --prefix=source-ru/ origin ru`

to be finished docs...

---

Current languages being worked on:
- [x] English
- [ ] Russian (Sinon)


---
Disclaimer:

I in no way condone what is happening in Ukraine, and the only reason I give Russian as my examples is that it's the launage that I grew up with. I learned English as a second language. I do not know a third language to give examples with. 