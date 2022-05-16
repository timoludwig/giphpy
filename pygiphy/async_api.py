import typing

import httpx

from pygiphy.core import _handle_params
from pygiphy.core import _validate_weirdness
from pygiphy.core import async_get
from pygiphy.enums import Bundle
from pygiphy.enums import Rating
from pygiphy.enums import _Resource
from pygiphy.models import CategoryListResponse
from pygiphy.models import ChannelListResponse
from pygiphy.models import GifListResponse
from pygiphy.models import GifResponse
from pygiphy.models import RandomIdResponse
from pygiphy.models import SearchTermListResponse
from pygiphy.models import TermListResponse
from pygiphy.models import TrendingSearchTermsListResponse

__all__ = [
    "async_action_register",
    "async_autocomplete",
    "async_channel_search",
    "async_categories",
    "async_get_gif_by_id",
    "async_get_gifs_by_id",
    "async_random_id",
    "async_trending_search_terms",
    "async_gif_translate",
    "async_random_gif",
    "async_random_sticker",
    "async_search_gifs",
    "async_search_suggestions",
    "async_search_stickers",
    "async_sticker_translate",
    "async_trending_gifs",
    "async_trending_stickers",
]


async def async_search_gifs(
    q: str,
    *,
    lang: str = None,
    rating: Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: Bundle = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, GifListResponse]:
    """Search for gifs asynchronously by a query string.

    https://developers.giphy.com/docs/api/endpoint#search

    Args:
        q: search query term or phrase
        lang: specify language using a 2-letter ISO 639-1 language code.
        rating: filters results by specified rating
        limit: maximum number of objects to return. if not passed, 25
        offset: the starting position of results. if not passed, 0
        api_key: giphy api key
        random_id: an ID/proxy for a specific user.
        bundle: returns only renditions that correspond to the named bundle.
        serialize: defaults to False. if True, returns a `GifListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `GifListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(
        func_kwargs=kwargs,
        q=q,
        lang=lang,
        rating=rating.value if rating else None,
        limit=limit,
        offset=offset,
        api_key=api_key,
        random_id=random_id,
        bundle=bundle.value if bundle else None,
    )
    return await async_get(_Resource.search.gif, model=GifListResponse if serialize else None, params=params, **kwargs)


async def async_search_stickers(
    q: str,
    *,
    lang: str = None,
    rating: Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: Bundle = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, GifListResponse]:
    """Search for stickers asynchronously by using a query string.

    https://developers.giphy.com/docs/api/endpoint#search

    Args:
        q: search query term or phrase
        lang: specify language using a 2-letter ISO 639-1 language code.
        rating: filters results by specified rating
        limit: maximum number of objects to return. if not passed, 25
        offset: the starting position of results. if not passed, 0
        api_key: giphy api key
        random_id: an ID/proxy for a specific user.
        bundle: returns only renditions that correspond to the named bundle.
        serialize: defaults to False. if True, returns a `GifListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `GifListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(
        func_kwargs=kwargs,
        q=q,
        lang=lang,
        rating=rating.value if rating else None,
        limit=limit,
        offset=offset,
        api_key=api_key,
        random_id=random_id,
        bundle=bundle.value if bundle else None,
    )
    return await async_get(
        _Resource.search.sticker, model=GifListResponse if serialize else None, params=params, **kwargs
    )


async def async_trending_gifs(
    *,
    rating: Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: Bundle = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, GifListResponse]:
    """Get trending gifs asynchronously.

    https://developers.giphy.com/docs/api/endpoint#trending

    Args:
        rating: filters results by specified rating
        limit: maximum number of objects to return. if not passed, 25
        offset: the starting position of results. if not passed, 0
        api_key: giphy api key
        random_id: an ID/proxy for a specific user.
        bundle: returns only renditions that correspond to the named bundle.
        serialize: defaults to False. if True, returns a `GifListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `GifListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(
        func_kwargs=kwargs,
        rating=rating.value if rating else None,
        limit=limit,
        offset=offset,
        api_key=api_key,
        random_id=random_id,
        bundle=bundle.value if bundle else None,
    )
    return await async_get(
        _Resource.trending.gif, model=GifListResponse if serialize else None, params=params, **kwargs
    )


async def async_trending_stickers(
    *,
    rating: Rating = None,
    limit: int = None,
    offset: int = None,
    api_key: str = None,
    random_id: str = None,
    bundle: Bundle = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, GifListResponse]:
    """Get trending stickers asynchronously.

    https://developers.giphy.com/docs/api/endpoint#trending

    Args:
        rating: filters results by specified rating
        limit: maximum number of objects to return. if not passed, 25
        offset: the starting position of results. if not passed, 0
        api_key: giphy api key
        random_id: an ID/proxy for a specific user.
        bundle: returns only renditions that correspond to the named bundle.
        serialize: defaults to False. if True, returns a `GifListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        GifListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(
        func_kwargs=kwargs,
        rating=rating.value if rating else None,
        limit=limit,
        offset=offset,
        api_key=api_key,
        random_id=random_id,
        bundle=bundle.value if bundle else None,
    )
    return await async_get(
        _Resource.trending.sticker, model=GifListResponse if serialize else None, params=params, **kwargs
    )


async def async_gif_translate(
    s: str, *, api_key: str = None, weirdness: int = None, random_id: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, GifResponse]:
    """Asynchronously translate words or phrases to a single gif.

    https://developers.giphy.com/docs/api/endpoint#translate

    Args:
        s: search term
        api_key: giphy api key
        weirdness ('int', `optional`): value from 0-10 which makes results weirder as you go up the scale
        random_id: an ID/proxy for a specific user
        serialize: defaults to False. if True, returns a `GifResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `GifResponse` if serialize is True, else `httpx.Response`
    """
    _validate_weirdness(weirdness)
    params = _handle_params(func_kwargs=kwargs, s=s, weirdness=weirdness, api_key=api_key, random_id=random_id)
    return await async_get(_Resource.translate.gif, params=params, model=GifResponse if serialize else None, **kwargs)


async def async_sticker_translate(
    s: str, *, api_key: str = None, weirdness: int = None, random_id: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, GifResponse]:
    """Asynchronously translate words or phrases to a single sticker.

    https://developers.giphy.com/docs/api/endpoint#translate

    Args:
        s: search term
        api_key: giphy api key
        weirdness ('int', `optional`): value from 0-10 which makes results weirder as you go up the scale
        random_id: an ID/proxy for a specific user
        serialize: defaults to False. if True, returns a `GifResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `GifResponse` if serialize is True, else `httpx.Response`
    """
    _validate_weirdness(weirdness)
    params = _handle_params(func_kwargs=kwargs, s=s, weirdness=weirdness, api_key=api_key, random_id=random_id)
    return await async_get(
        _Resource.translate.sticker, params=params, model=GifResponse if serialize else None, **kwargs
    )


async def async_random_gif(
    *,
    api_key: str = None,
    tag: str = None,
    rating: Rating = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, GifResponse]:
    """Get a single random GIF asynchronously

     https://developers.giphy.com/docs/api/endpoint#random

     Args:
         api_key: giphy api key
         tag ('str`, `optional`): filter results by a specified tag
         rating: filters results by specified rating
         random_id: an ID/proxy for a specific user
         serialize: defaults to False. if True, returns a `GifResponse` object
         **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
         `GifResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(
        func_kwargs=kwargs, api_key=api_key, tag=tag, rating=rating.value if rating else None, random_id=random_id
    )
    return await async_get(_Resource.random.gif, params=params, model=GifResponse if serialize else None, **kwargs)


async def async_random_sticker(
    *,
    api_key: str = None,
    tag: str = None,
    rating: Rating = None,
    random_id: str = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, GifResponse]:
    """Get a single random sticker asynchronously

     https://developers.giphy.com/docs/api/endpoint#random

     Args:
         api_key: giphy api key
         tag ('str`, `optional`): filter results by a specified tag
         rating: filters results by specified rating
         random_id: an ID/proxy for a specific user
         serialize: defaults to False. if True, returns a `GifResponse` object
         **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
         `GifResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(
        func_kwargs=kwargs, api_key=api_key, tag=tag, rating=rating.value if rating else None, random_id=random_id
    )
    return await async_get(_Resource.random.sticker, params=params, model=GifResponse if serialize else None, **kwargs)


async def async_random_id(
    *, api_key: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, RandomIdResponse]:
    """Asynchronously generate a unique ID you can assign to each new user in your app.

    https://developers.giphy.com/docs/api/endpoint#random-id

    Args:
        api_key: giphy api key
        serialize: defaults to False. if True, returns a `RandomIdResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `RandomIdResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, api_key=api_key)
    return await async_get("/randomid", model=RandomIdResponse if serialize else None, params=params, **kwargs)


async def async_action_register(url: str, random_id: str, ts: int, *, api_key: str = None, **kwargs) -> httpx.Response:
    """Asynchronously Register an impression, click, or send sing a callback url from the analytics object.

    https://developers.giphy.com/docs/api/endpoint#action-register

    Args:
        url: an impression, on click, or send callback url from the analytics object
        random_id: an id/proxy for a specific user
        ts: a unix timestamp in milliseconds corresponding to when the action occurred
        api_key: giphy api key
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, api_key=api_key, random_id=random_id, ts=ts)
    return await async_get(url, params=params, **kwargs)


async def async_get_gif_by_id(
    gif_id: str, *, api_key: str = None, random_id: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, GifResponse]:
    """Get a single gif asynchronously by its unique identifier

    https://developers.giphy.com/docs/api/endpoint#get-gif-by-id

    Args:
        gif_id: the unique identifier of the gif you want details for
        api_key: giphy api key
        random_id: an id/proxy for a specific user
        serialize: defaults to False. if True, returns a `GifResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `GifResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, api_key=api_key, random_id=random_id)
    return await async_get(f"/gifs/{gif_id}", model=GifResponse if serialize else None, params=params, **kwargs)


async def async_get_gifs_by_id(
    *gif_ids: str,
    api_key: str = None,
    random_id: str = None,
    serialize: bool = None,
    **kwargs,
) -> typing.Union[httpx.Response, GifListResponse]:
    """Get one or more gifs asynchronously by their unique identifiers.

    https://developers.giphy.com/docs/api/endpoint#get-gifs-by-id

    Args:
        *gif_ids: any number of unique identifiers for gifs you want details for
        api_key: giphy api key
        random_id: an id/proxy for a specific user
        serialize: defaults to False. if True, returns a `GifListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `GifListResponse` if serialize is True, else `httpx.Response`
    """
    str_gif_ids = ",".join(gif_ids)
    params = _handle_params(func_kwargs=kwargs, ids=str_gif_ids, api_key=api_key, random_id=random_id)
    return await async_get(f"/gifs", params=params, model=GifListResponse if serialize else None, **kwargs)


async def async_categories(
    *, api_key: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, CategoryListResponse]:
    """Asynchronously get a list of gif categories on the giphy network.

    https://developers.giphy.com/docs/api/endpoint#categories

    Args:
        api_key: giphy api key
        serialize: defaults to False. if True, returns a `CategoryListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `CategoryListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, api_key=api_key)
    return await async_get(
        "/gifs/categories", model=CategoryListResponse if serialize else None, params=params, **kwargs
    )


async def async_autocomplete(
    q: str, *, api_key: str = None, limit: int = None, offset: int = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, SearchTermListResponse]:
    """Asynchronously provides a list of valid terms that completes the given tag on the giphy network

    https://developers.giphy.com/docs/api/endpoint#autocomplete

    Args:
        q: tag term
        api_key: giphy api key
        limit: maximum number of objects to return. if not passed, 25
        offset: the starting position of results. if not passed, 0
        serialize: defaults to False. if True, returns a `SearchTermListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `SearchTermListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, q=q, api_key=api_key, limit=limit, offset=offset)
    return await async_get(
        "gifs/search/tags", params=params, model=SearchTermListResponse if serialize else None, **kwargs
    )


async def async_channel_search(
    q: str, *, api_key: str = None, limit: int = None, offset: int = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, ChannelListResponse]:
    """Asynchronously returns all the giphy channels matching the query term.

    https://developers.giphy.com/docs/api/endpoint#channel-search

    Args:
        q: accepts term to search through giphy’s channels
        api_key: giphy api key
        limit: maximum number of objects to return. if not passed, 25
        offset: the starting position of results. if not passed, 0
        serialize: defaults to False. if True, returns a `ChannelListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `ChannelListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, q=q, api_key=api_key, limit=limit, offset=offset)
    return await async_get(
        "/channels/search", params=params, model=ChannelListResponse if serialize else None, **kwargs
    )


async def async_search_suggestions(
    term: str, *, api_key: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, TermListResponse]:
    """Asynchronously provides a list of tag terms related to the given tag on the giphy network.

    https://developers.giphy.com/docs/api/endpoint#search-suggestions

    Args:
        term: tag term
        api_key: giphy api key
        serialize: defaults to False. if True, returns a `TermListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `TermListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, api_key=api_key)
    return await async_get(
        f"/tags/related/{term}", params=params, model=TermListResponse if serialize else None, **kwargs
    )


async def async_trending_search_terms(*, api_key: str = None, serialize: bool = False, **kwargs):
    """Asynchronously provides a list of the most popular trending search terms on the giphy network.

    https://developers.giphy.com/docs/api/endpoint#trending-search-terms

    Args:
        api_key: giphy api key
        serialize: defaults to False. if True, returns a `TermListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.AsyncClient.get`

    Returns:
        `TrendingSearchTermsListResponse` if serialize is True, else `httpx.Response`
    """
    params = _handle_params(func_kwargs=kwargs, api_key=api_key)
    return await async_get(
        "/trending/searches", params=params, model=TrendingSearchTermsListResponse if serialize else None, **kwargs
    )
