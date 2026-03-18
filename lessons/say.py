# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
# pyright: reportAttributeAccessIssue=false

# import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.beavis("hello, " + sys.argv[1])

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])


print("file name: ", __name__)
