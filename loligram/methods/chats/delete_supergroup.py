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


class DeleteSupergroup:
    async def delete_supergroup(
        self: "loligram.Client",
        chat_id: Union[int, str]
    ) -> bool:
        """Delete a supergroup.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The id of the supergroup to be deleted.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.delete_supergroup(supergroup_id)
        """
        await self.invoke(
            raw.functions.channels.DeleteChannel(
                channel=await self.resolve_peer(chat_id)
            )
        )

        return True
