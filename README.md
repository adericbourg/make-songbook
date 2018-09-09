# make-songbook

> make-songbook builds a ePub to bring your songs and tablatures into an eInk reader

Your library has to be structured by artist and by song.

Example:

```plain
.
├── Mark Lanegan
│   ├── The Cherry tree Carol.txt
└── The Rolling Stones
    ├── Brown Sugar.txt
    └── Sympathy for the Devil.txt
```

Running `make-songbook` will produce a single ePub containing all songs in that folder including a table of contents.

Example:

```bash
make-songbook MyLibrary
```

The songbook will be located at the root of your song library (inside `MyLibrary` for the given example).

> For simplicity reasons, only ePub format is currently supported. There is no plan to support any other format for now.
> If you need to use another format, you may use [Calibre](https://calibre-ebook.com/) that is able to convert your ePub
> to many other formats (mobi, azw3 or even PDF).
