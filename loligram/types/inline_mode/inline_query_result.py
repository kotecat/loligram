#  Loligram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Loligram.
#
#  Loligram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Loligram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Loligram.  If not, see <http://www.gnu.org/licenses/>.

from uuid import uuid4

import loligram
from loligram import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~loligram.types.InlineQueryResultCachedAudio`
    - :obj:`~loligram.types.InlineQueryResultCachedDocument`
    - :obj:`~loligram.types.InlineQueryResultCachedAnimation`
    - :obj:`~loligram.types.InlineQueryResultCachedPhoto`
    - :obj:`~loligram.types.InlineQueryResultCachedSticker`
    - :obj:`~loligram.types.InlineQueryResultCachedVideo`
    - :obj:`~loligram.types.InlineQueryResultCachedVoice`
    - :obj:`~loligram.types.InlineQueryResultArticle`
    - :obj:`~loligram.types.InlineQueryResultAudio`
    - :obj:`~loligram.types.InlineQueryResultContact`
    - :obj:`~loligram.types.InlineQueryResultDocument`
    - :obj:`~loligram.types.InlineQueryResultAnimation`
    - :obj:`~loligram.types.InlineQueryResultLocation`
    - :obj:`~loligram.types.InlineQueryResultPhoto`
    - :obj:`~loligram.types.InlineQueryResultVenue`
    - :obj:`~loligram.types.InlineQueryResultVideo`
    - :obj:`~loligram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "loligram.Client"):
        pass
