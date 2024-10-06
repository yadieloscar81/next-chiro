# import os

# from alembic import context
# from sqlalchemy import engine_from_config, pool
# from app.models.user import SQLModel

# target_metadata = SQLModel.metadata
# from app.config.config import settings

# config = context.config


# def get_url():
#     return str(settings.DATABASE_URL)

# def run_migrations_offline():
#     """Run migrations in 'offline' mode.

#     This configures the context with just a URL
#     and not an Engine, though an Engine is acceptable
#     here as well.  By skipping the Engine creation
#     we don't even need a DBAPI to be available.

#     Calls to context.execute() here emit the given string to the
#     script output.

#     """
#     url = get_url()
#     context.configure(
#         url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True
#     )

#     with context.begin_transaction():
#         context.run_migrations()


# def run_migrations_online():
#     """Run migrations in 'online' mode.

#     In this scenario we need to create an Engine
#     and associate a connection with the context.

#     """
#     configuration = config.get_section(config.config_ini_section)
#     configuration["sqlalchemy.url"] = get_url()
#     connectable = engine_from_config(
#         configuration,
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=target_metadata, compare_type=True
#         )

#         with context.begin_transaction():
#             context.run_migrations()


# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()