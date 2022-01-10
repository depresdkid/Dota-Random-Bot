"""List of WebAPI endpoints."""
# Спижжено с d2api для добавления своих эндпоитнов
ROOT_URL = "https://api.steampowered.com"

# IDOTA2Match_570
GET_MATCH_HISTORY = ROOT_URL + "/IDOTA2Match_570/GetMatchHistory/v001/"
GET_MATCH_HISTORY_BY_SEQ_NUM = ROOT_URL + "/IDOTA2Match_570/GetMatchHistoryBySequenceNum/v0001/"
GET_MATCH_DETAILS = ROOT_URL + "/IDOTA2Match_570/GetMatchDetails/v001/"
GET_LIVE_LEAGUE_GAMES = ROOT_URL + "/IDOTA2Match_570/GetLiveLeagueGames/v0001/"
GET_TEAM_INFO_BY_TEAM_ID = ROOT_URL + "/IDOTA2Match_570/GetTeamInfoByTeamID/v001/"
GET_TOP_LIVE_GAME = ROOT_URL + "/IDOTA2Match_570/GetTopLiveGame/v1/"

# IEconDOTA2_570
GET_TOURNAMENT_PRIZE_POOL = ROOT_URL + "/IEconDOTA2_570/GetTournamentPrizePool/v1/"
GET_ITEM_ICON_PATH = ROOT_URL + "/IEconDOTA2_570/GetItemIconPath/v1"
GET_GAME_ITEMS = ROOT_URL + "/IEconDOTA2_570/GetGameItems/v0001/"
GET_RARITIES = ROOT_URL + "/IEconDOTA2_570/GetRarities/v1"
GET_HEROES = ROOT_URL + "/IEconDOTA2_570/GetHeroes/v0001/"

# IDOTA2StreamSystem_570
GET_BROADCASTER_INFO = ROOT_URL + "/IDOTA2StreamSystem_570/GetBroadcasterInfo/v1"

# ISteamUser
GET_PLAYER_SUMMARIES = ROOT_URL + "/ISteamUser/GetPlayerSummaries/v0002/"