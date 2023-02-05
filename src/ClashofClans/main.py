from typing import Any
from .request import request, remove_hashtag, add_kwargs


class ClashofClans:
    """
    Always returns tuple[code, response, response_json]
    code: returns the https response code as an int
    response: returns the raw response
    response_json: returns the data from response.json()

    Official Documentation: https://developer.clashofclans.com/#/documentation
    """

    def __init__(self, apitoken):
        self.apitoken = apitoken

        self.clans = self.clans(apitoken)
        self.players = self.players(apitoken)
        self.leagues = self.leagues(apitoken)
        self.locations = self.locations(apitoken)
        self.goldpass = self.goldpass(apitoken)
        self.esports = self.esports(apitoken)
        self.labels = self.labels(apitoken)

    class clans:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def get_currentwar_leaguegroup(self, clanTag: str) -> tuple[Any, Any, Any]:  # should be fine
            """/clans/%23{clanTag}/currentwar/leaguegroup \n Retrieve information about clan's current clan war
            league group """
            return request(f"/clans/%23{remove_hashtag(clanTag)}/currentwar/leaguegroup", self.apitoken)

        def get_warleagueinfo(self, warTag: str) -> tuple[Any, Any, Any]:
            """/clanwarleagues/wars/{warTag} \n Retrieve information about individual clan war league war"""
            return request(f"/clanwarleagues/wars/%23{remove_hashtag(warTag)}", self.apitoken)

        def get_warlog(self, clanTag, **kwargs) -> tuple[Any, Any, Any]:  # after and before doesn't work
            """/clans/{clanTag}/warlog \n Retrieve clan's clan war log\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/clans/%23{remove_hashtag(clanTag)}/warlog", **kwargs), self.apitoken)  # &after={after}&before={before}", self.apitoken)

        def search(self, **kwargs) -> tuple[Any, Any, Any]:
            """/clans \n Search all clans by name and/or filtering the results using various criteria. At least one filtering criteria must be defined and if name is
            used as part of search, it is required to be at least three characters long. It is not possible to specify ordering for results so clients should not rely
            on any specific ordering as that may change in the future releases of the API.

            kwargs: name: str, warFrequency: str = "", locationId: int = "", minMembers: int = 1, maxMembers: int = 50, minClanPoints: int = 0,
            minClanLevel: int = 0, limit: int = 100000, after: str = "", before: str = "", labelIds: str = ""
            """
            return request(add_kwargs(f"/clans", **kwargs), self.apitoken)

        def get_currentwar(self, clanTag) -> tuple[Any, Any, Any]:
            """# /clans/{clanTag}/currentwar \n Retrieve information about clan's current clan war"""
            return request(f"/clans/%23{remove_hashtag(clanTag)}/currentwar", self.apitoken)

        def get_info(self, clanTag) -> tuple[Any, Any, Any]:
            """/clans/{clanTag}\nGet information about a single clan by clan tag. Clan tags can be found using clan search operation"""
            return request(f"/clans/%23{remove_hashtag(clanTag)}", self.apitoken)

        def get_memberlist(self, clanTag, **kwargs) -> tuple[Any, Any, Any]:  # after and before doesn't work
            """/clans/{clanTag}/members\nList clan members\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/clans/%23{remove_hashtag(clanTag)}/members", **kwargs), self.apitoken)  # &after={after}&before={before}", self.apitoken)

        def get_capitalraidseason(self, clanTag, **kwargs) -> tuple[Any, Any, Any]:  # after and before doesn't work
            """/clans/{clanTag}/capitalraidseasons\nRetrieve clan's capital raid seasons\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/clans/%23{remove_hashtag(clanTag)}/capitalraidseasons", **kwargs), self.apitoken)  # &after={after}&before={before}")

    class players:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def get_player_info(self, playerTag) -> tuple[Any, Any, Any]:
            """/players/{playerTag}\nGet information about a single player by player tag. Player tags can be found either in game or from clan member lists."""
            return request(f"/players/%23{remove_hashtag(playerTag)}", self.apitoken)

        def verifytoken(self, playerTag, token) -> tuple[Any, Any, Any]:
            """/players/{playerTag}/verifytoke
            Verify player API token that can be found from the game settings. This API call can be used to check that players
            own the game accounts they claim to own as they need to provide the one-time use API token that exists inside the game. """
            return request(f"/players/%23{remove_hashtag(playerTag)}/verifytoken", self.apitoken, "POST", {"token": str(token)})

    class leagues:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def list_capital_leagues(self, **kwargs):
            """/capitalleagues\nList capital leagues\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs("/capitalleagues", **kwargs), self.apitoken)

        def list_leagues(self, **kwargs):
            """/leagues\nList leagues\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs("/leagues", **kwargs), self.apitoken)

        def get_league_season_rankings(self, leagueId: str, seasonId: str, **kwargs):
            """/leagues/{leagueId}/seasons/{seasonId}
            Get league season rankings. Note that league season information is available only for Legend League.
            kwargs: limit: int, after: str, before: str"""
            request(add_kwargs(f"/leagues/{leagueId}/seasons/{seasonId}", **kwargs), self.apitoken)

        def get_capital_league_info(self, leagueId: str):
            """/capitalleagues/{leagueId}\nGet capital league information"""
            return request(f"/capitalleagues/{leagueId}", self.apitoken)

        def get_league_info(self, leagueId: str):
            """/leagues/{leagueId}\nGet league information"""
            return request(f"/leagues/{leagueId}", self.apitoken)

        def get_league_seasons(self, leagueId: str, **kwargs):
            """/leagues/{leagueId}/seasons
            Get league seasons. Note that league season information is available only for Legend League.
            kwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/leagues/{leagueId}/seasons", **kwargs), self.apitoken)

        def get_warleague_info(self, leagueId: str):
            """/warleagues/{leagueId}\nGet war league information"""
            return request(f"/warleagues/{leagueId}", self.apitoken)

        def list_warleagues(self, **kwargs):
            """/warleagues\nList war leagues\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs("/warleagues", **kwargs), self.apitoken)

    class locations:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def get_clan_rankings(self, locationId: str, **kwargs):
            """/locations/{locationId}/rankings/clans\nGet clan rankings for a specific location\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/locations/{locationId}/rankings/clans", **kwargs), self.apitoken)

        def get_player_rankings(self, locationId: str, **kwargs):
            """/locations/{locationId}/rankings/players\nGet player rankings for a specific location\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/locations/{locationId}/rankings/players", **kwargs), self.apitoken)

        def get_clan_versus_rankings(self, locationId, **kwargs):
            """/locations/{locationId}/rankings/clans-versus\nGet clan versus rankings for a specific location\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/locations/{locationId}/rankings/clans-versus", **kwargs), self.apitoken)

        def get_player_versus_rankings(self, locationId, **kwargs):
            """/locations/{locationId}/rankings/players-versus\nGet player versus rankings for a specific location\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/locations/{locationId}/rankings/players-versus", **kwargs), self.apitoken)

        def list_locations(self, **kwargs):
            """/locations\nList locations\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs("/locations", **kwargs), self.apitoken)

        def get_capital_rankings(self, locationId: str, **kwargs):
            """/locations/{locationId}/rankings/capitals\nGet capital rankings for a specific location\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs(f"/locations/{locationId}/rankings/capitals", **kwargs), self.apitoken)

        def get_location_info(self, locationId):
            """/locations/{locationId}\nGet information about specific location"""
            return request(f"/locations/{locationId}", self.apitoken)

    class goldpass:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def getinfo(self):
            """/goldpass/seasons/current\nGet information about the current gold pass season."""
            return request("/goldpass/seasons/current", self.apitoken)

    class esports:
        def __init__(self, apitoken):
            self.apitoken = apitoken

    class labels:
        def __init__(self, apitoken):
            self.apitoken = apitoken

        def list_player_labels(self, **kwargs):
            """/labels/players\nList player labels\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs("/labels/players", **kwargs), self.apitoken)

        def list_clan_labels(self, **kwargs):
            """/labels/clans\nList clan labels\nkwargs: limit: int, after: str, before: str"""
            return request(add_kwargs("/labels/clans", **kwargs), self.apitoken)
