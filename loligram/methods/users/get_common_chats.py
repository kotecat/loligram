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

from typing import Union, List

import loligram
from loligram import raw
from loligram import types


class GetCommonChats:
    async def get_common_chats(
        self: "loligram.Client",
        user_id: Union[int, str]
    ) -> List["types.Chat"]:
        """Get the common chats you have with a user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            List of :obj:`~loligram.types.Chat`: On success, a list of the common chats is returned.

        Raises:
            ValueError: If the user_id doesn't belong to a user.

        Example:
            .. code-block:: python

                common = await app.get_common_chats(user_id)
                print(common)
        """

        peer = await self.resolve_peer(user_id)

        if isinstance(peer, raw.types.InputPeerUser):
            r = await self.invoke(
                raw.functions.messages.GetCommonChats(
                    user_id=peer,
                    max_id=0,
                    limit=100,
                )
            )

            return types.List([types.Chat._parse_chat(self, x) for x in r.chats])

        raise ValueError(f'The user_id "{user_id}" doesn\'t belong to a user')
