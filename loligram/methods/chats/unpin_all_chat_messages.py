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


class UnpinAllChatMessages:
    async def unpin_all_chat_messages(
        self: "loligram.Client",
        chat_id: Union[int, str],
    ) -> bool:
        """Use this method to clear the list of pinned messages in a chat.
        If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have
        the 'can_pin_messages' admin right in a supergroup or 'can_edit_messages' admin right in a channel.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Unpin all chat messages
                await app.unpin_all_chat_messages(chat_id)
        """
        await self.invoke(
            raw.functions.messages.UnpinAllMessages(
                peer=await self.resolve_peer(chat_id)
            )
        )

        return True
