from password_hack_tutorial import generators
from password_hack_tutorial import logics
from password_hack_tutorial import queries

# >>> Only one accaunt <<<
# logics.basic_logic(
#     login_generator=generators.BasicLoginsGenerator(),
#     password_generator=generators.FileLinesGenerator(filename='bad_passwords.txt'),
#     query=queries.request_local_server
# )

# >>> All accaunts pas -> login <<<
# logics.password_then_login_logic(
#     login_generator=generators.BasicLoginsGenerator(),
#     password_generator=generators.FileLinesGenerator(filename='bad_passwords.txt'),
#     query=queries.request_local_server
# )

# >>> All logins and all passwords <<<
# logics.password_then_login_logic(
#     login_generator=generators.FileLinesGenerator(filename='bad_passwords.txt'),
#     password_generator=generators.FileLinesGenerator(filename='bad_passwords.txt'),
#     query=queries.request_local_server
# )

# >>> All accaunts login -> pas <<<
# logics.login_then_password_logic(
#     login_generator=generators.BasicLoginsGenerator(),
#     password_generator=generators.FileLinesGenerator(filename='bad_passwords.txt'),
#     query=queries.request_local_server,
#     passwords_limit=10000
# )

# >>> All logins brut force<<<
logics.login_then_password_logic(
    login_generator=generators.BasicLoginsGenerator(),
    password_generator=generators.BruteForceGenerator(),
    query=queries.request_local_server,
    passwords_limit=200000000
)
