import logging
from asyncpg.exceptions import UniqueViolationError

logger = logging.getLogger(__name__)


async def insert_to_database(app, data_to_insert):
    for offer in data_to_insert:
        try:
            await app.db.insert(
                f"""
                            INSERT INTO public.flats
                            ({', '.join(offer.keys())})
                            VALUES({', '.join(f'${x + 1}' for x in range(len(offer)))})
                        """,
                list(offer.values())
            )
        except UniqueViolationError as e:
            logger.error(e)


async def extract_data_to_notify(app):
    """
    Here select interesting offers to notify in tg
    in where defined additional filters, for example,
    distance from center less than 30 km and defined period for which offers were created
    :param app:
    :return:
    """
    notification_data = await app.db.select(
        f"""
            SELECT added_timestamp,
                total_area,
                full_url, 
                jk_url,
                nearest_underground, 
                nearest_underground_dist, 
                price_rur, 
                rooms_count,
                is_apartments
            FROM public.flats
            WHERE 1=1 
                AND created_at > (now() - interval '1 hours' - interval '1 minute')
               -- AND distance_from_center <= 9
        """, {}
    )
    return notification_data
