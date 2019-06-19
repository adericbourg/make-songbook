extern crate clap;

use clap::{App, Arg};

fn main() {
    let _ = App::new("make-songbook")
        .version("0.1.0")
        .about("make-songbook builds an ePub to bring your songs and tablatures into an eInk reader")
        .author("Alban Dericbourg <alban@dericbourg.net>")
        .arg(Arg::with_name("library")
            .help("Sets the root location of your library")
            .required(true))
        .get_matches();
}
