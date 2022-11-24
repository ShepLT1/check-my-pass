# check-my-pass

Python-based "have I been hacked?" checker. Utilizes pwnedpasswords API & avoids sending full hashes across networks. Supports multiple password checks at once.

## Usage

Clone the repository, open the check-my-pass directory in your command line, & run the following command:

```console
python check.py <pass1> <pass2> <pass3>
```

## Responses

### Success

```
<pass1> was hacked 10579459 times... consider updating your password.
```

or

```
<pass1> has not been hacked.
```

### Error

```
Error fetching: 400, check API & try again
```
