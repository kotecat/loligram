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

import logging

import loligram
from loligram import raw
from loligram import types

log = logging.getLogger(__name__)


class ResendCode:
    async def resend_code(
        self: "loligram.Client",
        phone_number: str,
        phone_code_hash: str
    ) -> "types.SentCode":
        """Re-send the confirmation code using a different type.

        The type of the code to be re-sent is specified in the *next_type* attribute of the
        :obj:`~loligram.types.SentCode` object returned by :meth:`send_code`.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            phone_number (``str``):
                Phone number in international format (includes the country prefix).

            phone_code_hash (``str``):
                Confirmation code identifier.

        Returns:
            :obj:`~loligram.types.SentCode`: On success, an object containing information on the re-sent confirmation
            code is returned.

        Raises:
            BadRequest: In case the arguments are invalid.
        """
        phone_number = phone_number.strip(" +")

        r = await self.invoke(
            raw.functions.auth.ResendCode(
                phone_number=phone_number,
                phone_code_hash=phone_code_hash
            )
        )

        return types.SentCode._parse(r)
