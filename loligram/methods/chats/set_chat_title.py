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

from typing import Union

import loligram
from loligram import raw


class SetChatTitle:
    async def set_chat_title(
        self: "loligram.Client",
        chat_id: Union[int, str],
        title: str
    ) -> bool:
        """Change the title of a chat.
        Titles can't be changed for private chats.
        You must be an administrator in the chat for this to work and must have the appropriate admin rights.

        Note:
            In regular groups (non-supergroups), this method will only work if the "All Members Are Admins"
            setting is off.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            title (``str``):
                New chat title, 1-255 characters.

        Returns:
            ``bool``: True on success.

        Raises:
            ValueError: In case a chat id belongs to user.

        Example:
            .. code-block:: python

                await app.set_chat_title(chat_id, "New Title")
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChat):
            await self.invoke(
                raw.functions.messages.EditChatTitle(
                    chat_id=peer.chat_id,
                    title=title
                )
            )
        elif isinstance(peer, raw.types.InputPeerChannel):
            await self.invoke(
                raw.functions.channels.EditTitle(
                    channel=peer,
                    title=title
                )
            )
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user')

        return True
