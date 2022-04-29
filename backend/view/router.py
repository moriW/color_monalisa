#! /usr/bin/env python
# backend
# router entry
#
# @file: web
# @time: 2022/4/29
# @author: Mori
#

from tornado.web import RequestHandler

class HealthHandler(RequestHandler):
    async def get(self):
        self.write("health")
        await self.flush()

HANDLERS = [
    (r"/_health", HealthHandler),
]

__all__ = ["HANDLERS"]