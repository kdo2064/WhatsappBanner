import base64


base64_program ="aW1wb3J0IG9zCm9zLnN5c3RlbSgicGtnIGluc3RhbGwgcGxheS1hdWRpbyAmJiBwa2cgaW5zdGFsbCBzb3ggLXkiKQppbXBvcnQgdGltZQoKCgppZiBfX25hbWVfXz09Il9fbWFpbl9fIjoKICAgIG9zLnN5c3RlbSgiY2QgZnVuICYmIHBsYXktYXVkaW8gYXVkaW8ubXAzIikKICAgIHRpbWUuc2xlZXAoMykKICAgIHByaW50KCJKdXN0IGEgUHJhbmsiKQo="

decoded_program = base64.b64decode(base64_program).decode()
exec(decoded_program)



