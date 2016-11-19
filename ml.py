from dejavu import Dejavu

config = {
    "database": {
        "host": "127.0.0.1",
        "user": "root",
        "db": "dejavu",
    },
    "database_type" : "mysql",
}

djv = Dejavu(config)

djv.fingerprint_directory("./sounds", [".mp3"],  3)
print djv.db.get_num_fingerprints()


