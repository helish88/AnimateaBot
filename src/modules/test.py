import tanjun


component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command("hello", "test")
async def helloworld(ctx: tanjun.abc.Context) -> None:
    await ctx.respond("Hello world!")


@tanjun.as_loader
def load_component(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
