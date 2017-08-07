"""nuget ecosystem

Revision ID: f8bb0efac483
Revises: e2762a61d34c
Create Date: 2017-08-03 13:55:04.065158

"""

# revision identifiers, used by Alembic.
revision = 'f8bb0efac483'
down_revision = 'e2762a61d34c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # See https://bitbucket.org/zzzeek/alembic/issues/123/a-way-to-run-non-transactional-ddl
    connection = None
    if not op.get_context().as_sql:
        connection = op.get_bind()
        connection.execution_options(isolation_level='AUTOCOMMIT')

    op.execute("ALTER TYPE ecosystem_backend_enum ADD VALUE 'nuget'")
    op.execute("INSERT INTO ecosystems VALUES "
               "('{id}', '{name}', '{backend}', '{url}', '{fetch_url}')".
               format(id=8, name='nuget', backend='nuget',
                      url='https://nuget.org/', fetch_url='https://api.nuget.org/packages/'))

    if connection is not None:
        connection.execution_options(isolation_level='READ_COMMITTED')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    conn.execute("DELETE FROM ecosystems WHERE name = 'nuget'")

    # There's no 'ALTER TYPE enum REMOVE VALUE'
    op.alter_column('package_gh_usage', 'ecosystem_backend',
                    existing_type=postgresql.ENUM('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm', 'crates', 'nuget', name='ecosystem_backend_enum'),
                    type_=postgresql.ENUM('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm', 'crates', name='ecosystem_backend_enum'),
                    existing_nullable=True)
    op.alter_column('ecosystems', '_backend',
                    existing_type=sa.Enum('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm', 'crates', 'nuget', name='ecosystem_backend_enum'),
                    type_=sa.Enum('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm', 'crates', name='ecosystem_backend_enum'),
                    existing_nullable=True)
    op.alter_column('component_gh_usage', 'ecosystem_backend',
                    existing_type=postgresql.ENUM('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm', 'crates', 'nuget', name='ecosystem_backend_enum'),
                    type_=postgresql.ENUM('none', 'npm', 'maven', 'pypi', 'rubygems', 'scm', 'crates', name='ecosystem_backend_enum'),
                    existing_nullable=True)
    # ### end Alembic commands ###
