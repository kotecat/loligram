#  Loligram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present Loli <https://github.com/delivrance>
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

from typing import List, Callable

import loligram
from loligram.filters import Filter
from loligram.types import Message
from .handler import Handler


class DeletedMessagesHandler(Handler):
    """The deleted messages handler class. Used to handle deleted messages coming from any chat
    (private, group, channel). It is intended to be used with :meth:`~loligram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~loligram.Client.on_deleted_messages` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when one or more messages have been deleted.
            It takes *(client, messages)* as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of messages to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~loligram.Client`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        messages (List of :obj:`~loligram.types.Message`):
            The deleted messages, as list.
    """

    def __init__(self, callback: Callable, filters: Filter = None):
        super().__init__(callback, filters)

    async def check(self, client: "loligram.Client", messages: List[Message]):
        # Every message should be checked, if at least one matches the filter True is returned
        # otherwise, or if the list is empty, False is returned
        for message in messages:
            if await super().check(client, message):
                return True
        else:
            return False
