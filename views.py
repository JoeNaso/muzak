from __future__ import absolute_import

from models import Interface
from flask import Flask

muzak = Flask(__name__)


@muzak.route('/api/spotify-user/', methods=['GET'])
def spotify():
    sp = Interface().spotify

    return sp.endpoint_url('user')


@muzak.route('/api/songkick-user/', methods=['GET'])
def songkick():
    sk = Interface.songkick

    return sk.endpoint_url('user')


if __name__ == '__main__':
    muzak.run()
