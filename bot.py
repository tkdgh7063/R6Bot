import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
import func
import r6sapi as api
import os

r6bot = commands.Bot(command_prefix="//")
token = os.environ["BOT_TOKEN"]

users = {}

@r6bot.event
async def on_ready():
    print('ABC bot logged in as {0.user}'.format(r6bot))
    await r6bot.change_presence(activity=discord.Game(name=r6bot.command_prefix + "도움 for help | 레식 전적 봇"))


@r6bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        error_embed = discord.Embed(colour=discord.Colour.red())
        error_embed.title = "명령어 사용법이 잘못되었습니다."
        error_embed.description = "필수입력요소가 입력되지 않았습니다."
        if str(error.param) == "pref":
            error_embed.add_field(name="필수입력", value="프리픽스")
        if str(error.param) == "oper" or str(error.param) == "operator":
            error_embed.add_field(name="필수입력", value="오퍼레이터")
        if str(error.param) == "name":
            error_embed.add_field(name="필수입력", value="이름")
        await ctx.send(embed=error_embed)

    elif isinstance(error, commands.CommandNotFound):
        error_embed = discord.Embed(colour=discord.Colour.red())
        error_embed.title = "명령어가 존재하지 않습니다."
        error_embed.description = "`" + r6bot.command_prefix + "도움`으로 명령어를 볼 수 있습니다."
        await ctx.send(embed=error_embed)

    elif isinstance(error, KeyError):
        error_embed = discord.Embed(colour=discord.Colour.red())
        error_embed.title = "명령어 사용법이 잘못되었습니다."
        error_embed.description = "입력요소가 잘못 입력되었습니다."
        error_embed.add_field(name="잘못된 입력", value=error.__str__())
        await ctx.send(embed=error_embed)


@r6bot.command()
async def msg(ctx, args):
    await ctx.send("ctx:" + str(ctx))
    await ctx.send("ctx.message:" + str(ctx.message))
    await ctx.send("ctx.message.content:" + str(ctx.message.content))
    await ctx.send("args:" + str(args))
    await ctx.send("ctx.kwargs:" + str(ctx.kwargs))


@r6bot.command()
async def 도움(ctx):
    embed = discord.Embed(title="명령어 도움말", colour=discord.Colour.green())
    embed.description = "명령어 도움말이에요." \
                        "플랫폼과 지역은 생략시 UPLAY, ASIA로 검색합니다." \
                        "플랫폼: UPLAY, XBOX, PS | 지역: ASIA, EU, NA"
    embed.add_field(name=r6bot.command_prefix + "명령어 [프리픽스]", value="명령어 프리픽스를 변경합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "오퍼정보 [오퍼]", value="오퍼레이터의 정보를 검색합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "정보 [닉네임] [플랫폼]", value="유저의 정보를 검색합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "캐주얼 [닉네임] [플랫폼]", value="유저의 캐주얼 전적을 검색합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "랭크 [닉네임] [지역] [플랫폼]", value="유저의 랭크 전적을 검색합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "오퍼전적 [닉네임] [오퍼] [플랫폼]",
                    value="유저의 오퍼레이터 전적을 검색합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "공격오퍼타임 [닉네임] [숫자] [플랫폼]",
                    value="유저의 공격오퍼의 플레이타임 순으로 숫자 개수만큼 표시합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "공격오퍼킬뎃 [닉네임] [숫자] [플랫폼]",
                    value="유저의 공격오퍼의 킬뎃 순으로 숫자 개수만큼 표시합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "수비오퍼타임 [닉네임] [숫자] [플랫폼]",
                    value="유저의 수비오퍼의 플레이타임 순으로 숫자 개수만큼 표시합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "수비오퍼킬뎃 [닉네임] [숫자] [플랫폼]",
                    value="유저의 수비오퍼의 킬뎃 순으로 숫자 개수만큼 표시합니다.", inline=False)
    embed.add_field(name=r6bot.command_prefix + "팀 [닉네임] [플랫폼]",
                    value="닉네임으로 입력된 사람들의 팀을 구성해줍니다.", inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 명령어(ctx, pref):
    r6bot.command_prefix = str(pref)
    embed = discord.Embed()
    embed.title = discord.Embed.Empty
    embed.description = "명령어 프리픽스가 설정되었습니다."
    embed.colour = discord.Colour.green()
    embed.add_field(name="prefix", value=pref)
    await ctx.send(embed=embed)
    await r6bot.change_presence(activity=discord.Game(name=r6bot.command_prefix + "도움 for help | 레식 전적 봇"))


@r6bot.command()
async def 오퍼정보(ctx, oper):
    search = str(oper).lower()
    if search not in func.ALL:
        error = discord.Embed(colour=discord.Colour.red())
        error.title = "존재하지 않는 오퍼레이터입니다."
        oper_str = ""
        for i in func.ALL:
            oper_str += str(i).upper()
            if i != func.ALL.__getitem__(len(func.ALL) - 1):
                oper_str += ", "
        error.add_field(name="오퍼레이터 목록", value="```" + oper_str + "```")
        await ctx.send(embed=error)
    else:
        embed = discord.Embed(colour=discord.Colour.blue())
        UP = search.upper()
        embed.title = UP + " 대원 정보"
        embed.description = discord.Embed.Empty
        embed.set_thumbnail(url=func.BADGE[UP])
        embed.add_field(name="명칭", value=UP + "(" + func.KR_NAME[UP] + ")", inline=True)
        embed.add_field(name="부대", value=func.UNIT[UP], inline=True)
        if UP.lower() in func.ATT:
            embed.add_field(name="공격/수비", value="공격", inline=True)
        else:
            embed.add_field(name="공격/수비", value="수비", inline=True)
        embed.add_field(name="이름", value=func.NAME[UP], inline=True)
        embed.add_field(name="출생일", value=func.BIRTH[UP], inline=True)
        embed.add_field(name="출생지", value=func.HOME[UP], inline=True)
        embed.add_field(name="나이", value=func.AGE[UP], inline=True)
        embed.add_field(name="키", value=func.HEIGHT[UP], inline=True)
        embed.add_field(name="몸무게", value=func.WEIGHT[UP], inline=True)
        embed.add_field(name="속도", value=func.SP[UP], inline=True)
        embed.add_field(name="장갑", value=4 - func.SP[UP], inline=True)
        embed.add_field(name="특수능력", value=func.STAT_NAME[UP], inline=False)
        embed.add_field(name="설명", value=func.STAT_INST[UP], inline=False)
        embed.add_field(name="추가설명", value=func.STAT_ADD[UP], inline=False)
        await ctx.send(embed=embed)


@r6bot.command()
async def 정보(ctx, name, plat="UPLAY"):
    player = await func.get_info(name, plat)
    await player.load_level()
    await player.load_general()
    embed = discord.Embed(colour=discord.Colour.green())
    embed.set_thumbnail(url=player.icon_url)
    embed.title = player.name + "의 전적 개요"
    time_str = func.get_time_str(player.time_played)
    embed.add_field(name="닉네임", value=player.name, inline=True)
    embed.add_field(name="레벨", value=player.level, inline=True)
    embed.add_field(name="플레이시간", value=time_str, inline=True)
    embed.add_field(name="매치",
                    value="승리: " + str(player.matches_won) + " / 패배: " + str(player.matches_lost) +
                          "\n승률: " + str(round(player.matches_won / player.matches_played * 100, 2)) + "%",
                    inline=False)
    embed.add_field(name="전투",
                    value="사살: " + str(player.kills) + "(헤드샷:" + str(player.headshots) + ")" + " / 사망: " + str(
                        player.deaths) +
                          "\nKD: " + str(round(player.kills / player.deaths, 2)) +
                          "\n헤드샷비율: " + str(round(player.headshots / player.kills * 100, 2)) + "%",
                    inline=False)
    embed.add_field(name="기타",
                    value="사살 지원: " + str(player.kill_assists) + " / 관통 사살: " + str(
                        player.penetration_kills) + "\n근접 사살: " + str(player.melee_kills) +
                          " / 소생: " + str(player.revives),
                    inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 캐주얼(ctx, name, platform="UPLAY"):
    auth = func.get_Auth()
    plat = func.get_Plat(platform)
    player = await auth.get_player(str(name), str(plat))
    await player.load_queues()
    embed = discord.Embed(title=player.name + "의 캐주얼 전적", colour=discord.Colour.green())
    embed.set_thumbnail(url=player.icon_url)
    time_str = func.get_time_str(player.casual.time_played)
    embed.add_field(name="플레이 시간",
                    value=time_str)
    embed.add_field(name="매치",
                    value="승리: " + str(player.casual.won) + "/ 패배: " + str(player.casual.lost) +
                          "\n승률: " + str(round(player.casual.won / player.casual.played * 100, 2)) + "%",
                    inline=False)
    embed.add_field(name="전투",
                    value="사살: " + str(player.casual.kills) + " / 사망: " + str(player.casual.deaths) +
                          "\nKD: " + str(round(player.casual.kills / player.casual.deaths, 2)) +
                          "\n경기당 킬: " + str(round(player.casual.kills / player.casual.played, 2)) + "킬",
                    inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 랭크(ctx, name, region=api.RankedRegions.ASIA, platform="UPLAY"):
    auth = func.get_Auth()
    plat = func.get_Plat(str(platform))
    reg = func.get_Region(region)
    player = await auth.get_player(str(name), plat)
    await player.load_queues()
    ranks = await player.get_rank(region=reg)
    embed = discord.Embed(title=player.name + "의 랭크 전적", colour=discord.Colour.green())
    embed.set_thumbnail(url=ranks.get_icon_url())
    time_str = func.get_time_str(player.ranked.time_played)
    embed.add_field(name="플레이 시간",
                    value=time_str)
    embed.add_field(name="매치",
                    value="승리: " + str(player.ranked.won) + "/ 패배: " + str(player.ranked.lost) +
                          "\n승률: " + str(round(player.ranked.won / player.ranked.played * 100, 2)) + "%",
                    inline=False)
    embed.add_field(name="전투",
                    value="사살: " + str(player.ranked.kills) + " / 사망: " + str(player.ranked.deaths) +
                          "\nKD: " + str(round(player.ranked.kills / player.ranked.deaths, 2)) +
                          "\n경기당 킬: " + str(round(player.ranked.kills / player.ranked.played, 2)) + "킬",
                    inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 오퍼전적(ctx, name, oper, platform="UPLAY"):
    auth = func.get_Auth()
    plat = func.get_Plat(str(platform))
    player = await auth.get_player(str(name), plat)
    operator = await player.get_operator(str(oper))
    embed = discord.Embed()
    embed.title = player.name + "의 " + str(oper).upper() + " 전적"
    embed.colour = discord.Colour.green()
    embed.set_thumbnail(url=func.BADGE[str(oper).upper()])
    embed.add_field(name="경험치", value=operator.xp, inline=True)
    embed.add_field(name="플레이 타임", value=func.get_time_str(operator.time_played), inline=True)
    embed.add_field(name="라운드",
                    value="승리: " + str(operator.wins) + " / 패배: " + str(operator.losses) +
                          "\n승률: " + str(round(operator.wins / (operator.wins + operator.losses) * 100, 2)) + "%",
                    inline=False)
    embed.add_field(name="전투",
                    value="사살: " + str(operator.kills) + " / 사망: " + str(operator.deaths) +
                          "\nKD: " + str(round(operator.kills / operator.deaths, 2)),
                    inline=False)
    embed.add_field(name=func.STAT[str(oper).upper()], value=operator.statistic, inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 공격오퍼타임(ctx, name, num=2, plat="UPLAY"):
    auth = func.get_Auth()
    platform = func.get_Plat(plat)
    player = await auth.get_player(str(name), platform)
    operators = await player.get_all_operators()
    res = func.get_topAttTime(operators, num)
    embed = discord.Embed()
    embed.title = player.name + "의 플레이 타임순 공격대원"
    embed.colour = discord.Colour.green()
    embed.set_thumbnail(url=player.icon_url)
    for i in range(num):
        embed.add_field(name=res[i][0].upper() + "(" + func.KR_NAME[res[i][0].upper()] + ")",
                        value=func.get_time_str(res[i][1]) +
                              "\nKD: " + str(round(operators[res[i][0]].kills / operators[res[i][0]].deaths, 2)) +
                              "\n승률: " + str(round(
                            operators[res[i][0]].wins / (operators[res[i][0]].wins + operators[res[i][0]].losses) * 100,
                            2)) + "%",
                        inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 공격오퍼킬뎃(ctx, name, num=2, plat="UPLAY"):
    auth = func.get_Auth()
    platform = func.get_Plat(plat)
    player = await auth.get_player(str(name), platform)
    operators = await player.get_all_operators()
    res = func.get_topAttKD(operators, num)
    embed = discord.Embed()
    embed.title = player.name + "의 킬뎃순 공격대원"
    embed.colour = discord.Colour.green()
    embed.set_thumbnail(url=player.icon_url)
    for i in range(num):
        embed.add_field(name=res[i][0].upper() + "(" + func.KR_NAME[res[i][0].upper()] + ")",
                        value="KD: " + str(res[i][1]) + "\n플레이 타임: " + str(
                            func.get_time_str(operators[res[i][0]].time_played)) +
                              "\n승률: " + str(round(
                            operators[res[i][0]].wins / (operators[res[i][0]].wins + operators[res[i][0]].losses) * 100,
                            2)) + "%",
                        inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 수비오퍼타임(ctx, name, num=2, plat="UPLAY"):
    auth = func.get_Auth()
    platform = func.get_Plat(plat)
    player = await auth.get_player(str(name), platform)
    operators = await player.get_all_operators()
    res = func.get_topDefTime(operators, num)
    embed = discord.Embed()
    embed.title = player.name + "의 플레이 타임순 공격대원"
    embed.colour = discord.Colour.green()
    embed.set_thumbnail(url=player.icon_url)
    for i in range(num):
        embed.add_field(name=res[i][0].upper() + "(" + func.KR_NAME[res[i][0].upper()] + ")",
                        value=func.get_time_str(res[i][1]) +
                              "\nKD: " + str(round(operators[res[i][0]].kills / operators[res[i][0]].deaths, 2)) +
                              "\n승률: " + str(round(
                            operators[res[i][0]].wins / (operators[res[i][0]].wins + operators[res[i][0]].losses) * 100,
                            2)) + "%",
                        inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 수비오퍼킬뎃(ctx, name, num=2, plat="UPLAY"):
    auth = func.get_Auth()
    platform = func.get_Plat(plat)
    player = await auth.get_player(str(name), platform)
    operators = await player.get_all_operators()
    res = func.get_topDefKD(operators, num)
    embed = discord.Embed()
    embed.title = player.name + "의 킬뎃순 공격대원"
    embed.colour = discord.Colour.green()
    embed.set_thumbnail(url=player.icon_url)
    for i in range(num):
        embed.add_field(name=res[i][0].upper() + "(" + func.KR_NAME[res[i][0].upper()] + ")",
                        value="KD: " + str(res[i][1]) + "\n플레이 타임: " + str(func.get_time_str(operators[res[i][0]].time_played))+
                              "\n승률: " + str(round(operators[res[i][0]].wins / (operators[res[i][0]].wins + operators[res[i][0]].losses) * 100, 2)) + "%",
                        inline=False)
    await ctx.send(embed=embed)


@r6bot.command()
async def 팀(ctx, *args):
    plat = args[len(args) - 1]
    if plat != "UPLAY" and plat != "XBOX" and plat != "PS":
        plat = "UPLAY"
        num = len(args)
    else:
        num = len(args) - 1
    names = []
    for i in range(num):
        names.append(str(args[i]))
    res = await func.get_team(names, plat=plat)
    embed = discord.Embed()
    embed.title = "팀 결과"
    embed.colour = discord.Colour.from_rgb(0, 255, 255)
    orange = []
    blue = []
    for i in range(num):
        if i % 2 != 1:
            orange.append(res[i][0])
        else:
            blue.append(res[i][0])
    embed.add_field(name="주황팀", value=str(orange), inline=False)
    embed.add_field(name="파랑팀", value=str(blue), inline=False)
    await ctx.send(embed=embed)


r6bot.run(token)
