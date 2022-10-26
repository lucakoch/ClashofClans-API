from request import *


class coc:
    def __init__(self, apitoken):
        self.apitoken = apitoken

        self.clan = self.clan(apitoken)
        self.player = self.player(apitoken)
        self.league = self.league(apitoken)
        self.location = self.location(apitoken)
        self.goldpass = self.goldpass(apitoken)
        self.label = self.label(apitoken)

    def documentation(self):
        print("Documentation: https://developer.clashofclans.com/#/documentation")

    class clan:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def getcurrentwarleaguegroup(self, clantag):
            apitoken = self.apitoken

            clantag = rm_hashtag(clantag)
            response_json, response = request(f"https://api.clashofclans.com/v1/clans/%23{clantag}/currentwar/leaguegroup",
                                              apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getwarleagueinfo(self, wartag):
            apitoken = self.apitoken

            wartag = rm_hashtag(wartag)
            response_json, response = request(f"https://api.clashofclans.com/v1/clanwarleagues/wars/%23{wartag}", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getwarlog(self, clantag, limit=..., after=..., before=...):
            apitoken = self.apitoken

            clantag = rm_hashtag(clantag)
            link = f"https://api.clashofclans.com/v1/clans/%23{clantag}/warlog"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def search(self, name=..., warFrequency=..., locationId=..., minMembers=..., maxMembers=..., minClanPoints=...,
                        minClanLevel=..., limit=..., after=..., before=..., labelIds=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/clans"

            name_bool = False
            warFrequency_bool = False
            locationId_bool = False
            minMembers_bool = False
            maxMembers_bool = False
            minClanPoints_bool = False
            minClanLevel_bool = False
            limit_bool = False
            after_bool = False
            before_bool = False
            labelIds_bool = False

            if name is not ...:
                name_bool = True
            if warFrequency is not ...:
                warFrequency_bool = True
            if locationId is not ...:
                locationId_bool = True
            if minMembers is not ...:
                minMembers_bool = True
            if maxMembers is not ...:
                maxMembers_bool = True
            if minClanPoints is not ...:
                minClanPoints_bool = True
            if minClanLevel is not ...:
                minClanLevel_bool = True
            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True
            if labelIds is not ...:
                labelIds_bool = True

            if name_bool or warFrequency_bool or locationId_bool or minMembers_bool or maxMembers_bool or minClanPoints_bool or minClanLevel_bool or \
                    limit_bool or after_bool or before_bool or labelIds_bool == True:
                link += "?"

                if name_bool:
                    link += f"name={name}"
                if warFrequency_bool:
                    if name_bool:
                        link += f"&warFrequency={warFrequency}"
                    else:
                        link += f"warFrequency={warFrequency}"
                if locationId_bool:
                    if name_bool or warFrequency_bool:
                        link += f"&locationId={locationId}"
                    else:
                        link += f"locationId={locationId}"
                if minMembers_bool:
                    if name_bool or warFrequency_bool or locationId_bool:
                        link += f"&minMembers={minMembers}"
                    else:
                        link += f"minMembers={minMembers}"
                if maxMembers_bool:
                    if name_bool or warFrequency_bool or locationId_bool or minMembers_bool:
                        link += f"&maxMembers={maxMembers}"
                    else:
                        link += f"maxMembers={maxMembers}"
                if minClanPoints_bool:
                    if name_bool or warFrequency_bool or locationId_bool or minMembers_bool or maxMembers_bool:
                        link += f"&minClanPoints={minClanPoints}"
                    else:
                        link += f"minClanPoints={minClanPoints}"
                if minClanLevel_bool:
                    if name_bool or warFrequency_bool or locationId_bool or minMembers_bool or maxMembers_bool or minClanPoints_bool:
                        link += f"&minClanLevel={minClanLevel}"
                    else:
                        link += f"minClanLevel={minClanLevel}"
                if limit_bool:
                    if name_bool or warFrequency_bool or locationId_bool or minMembers_bool or maxMembers_bool or minClanPoints_bool or minClanLevel_bool:
                        link += f"&limit={limit}"
                    else:
                        link += f"limit={limit}"
                if after_bool:
                    if name_bool or warFrequency_bool or locationId_bool or minMembers_bool or maxMembers_bool or minClanPoints_bool or minClanLevel_bool or limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if name_bool or warFrequency_bool or locationId_bool or minMembers_bool or maxMembers_bool or minClanPoints_bool or minClanLevel_bool or limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"
                if labelIds_bool:
                    if name_bool or warFrequency_bool or locationId_bool or minMembers_bool or maxMembers_bool or minClanPoints_bool or minClanLevel_bool or limit_bool or after_bool or before_bool:
                        link += f"&labelIds={labelIds}"
                    else:
                        link += f"labelIds={labelIds}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getcurrentwar(self, clantag):
            apitoken = self.apitoken

            playertag = rm_hashtag(clantag)
            response_json, response = request(f"https://api.clashofclans.com/v1/clans/%23{playertag}/currentwar", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getinfo(self, clantag):
            apitoken = self.apitoken

            clantag = rm_hashtag(clantag)
            response_json, response = request(f"https://api.clashofclans.com/v1/clans/%23{clantag}", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getmemberinfo(self, clantag, limit=..., after=..., before=...):
            apitoken = self.apitoken

            clantag = rm_hashtag(clantag)
            link = f"https://api.clashofclans.com/v1/clans/%23{clantag}/members"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getcapitalraidseason(self, clantag, limit=..., after=..., before=...):
            apitoken = self.apitoken

            clantag = rm_hashtag(clantag)
            link = f"https://api.clashofclans.com/v1/clans/%23{clantag}/capitalraidseasons"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

    class player:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def getinfo(self, playertag):
                apitoken = self.apitoken

                playertag = rm_hashtag(playertag)
                response_json, response = request(f"https://api.clashofclans.com/v1/players/%23{playertag}", apitoken)

                code, answer, response_json = awnsers(response, response_json)
                return code, answer, response_json

        def verifyapitoken(self, playertag, token):
                apitoken = self.apitoken

                playertag = rm_hashtag(playertag)
                response_json, response = requestpost(f"https://api.clashofclans.com/v1/players/%23{playertag}/verifytoken",
                                                      apitoken, token)

                code, answer, response_json = awnsers(response, response_json)
                return code, answer, response_json

    class league:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def listleagues(self, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/leagues"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getleagueseasonrankings(self, leagueId, seasonId, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/leagues/{leagueId}/seasons/{seasonId}"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getleagueinfo(self, leagueId):
            apitoken = self.apitoken

            response_json, response = request(f"https://api.clashofclans.com/v1/leagues/{leagueId}", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getleagueseasons(self, leagueId):
            apitoken = self.apitoken

            response_json, response = request(f"https://api.clashofclans.com/v1/leagues/{leagueId}/seasons", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getwarleagueinfo(self, leagueId):
            apitoken = self.apitoken

            response_json, response = request(f"https://api.clashofclans.com/v1/warleagues/{leagueId}", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def listwarleagues(self, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/warleagues"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

    class location:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def getclanrankings(self, locationId, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/locations/{locationId}/rankings/clans"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getplayerrankings(self, locationId, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/locations/{locationId}/rankings/players"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getclanversusrankings(self, locationId, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/locations/{locationId}/rankings/clans-versus"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getplayerversusrankings(self, locationId, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/locations/{locationId}/rankings/players-versus"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def listlocations(self, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/locations"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def getlocationinfo(self, locationId):
            apitoken = self.apitoken

            response_json, response = request(f"https://api.clashofclans.com/v1/locations/{locationId}", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

    class goldpass:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def getinfo(self):
            apitoken = self.apitoken

            response_json, response = request(f"https://api.clashofclans.com/v1/goldpass/seasons/current", apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

    class label:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def listplayerlabels(self, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/labels/players"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json

        def listclanlabels(self, limit=..., after=..., before=...):
            apitoken = self.apitoken

            link = f"https://api.clashofclans.com/v1/labels/clans"

            limit_bool = False
            after_bool = False
            before_bool = False

            if limit is not ...:
                limit_bool = True
            if after is not ...:
                after_bool = True
            if before is not ...:
                before_bool = True

            if limit_bool or after_bool or before_bool == True:
                link += "?"

                if limit_bool:
                    link += f"limit={limit}"
                if after_bool:
                    if limit_bool:
                        link += f"&after={after}"
                    else:
                        link += f"after={after}"
                if before_bool:
                    if limit_bool or after_bool:
                        link += f"&before={before}"
                    else:
                        link += f"before={before}"

            response_json, response = request(link, apitoken)

            code, answer, response_json = awnsers(response, response_json)
            return code, answer, response_json
