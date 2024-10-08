"""Descripción de los cambios

Revision ID: d60cdbabefe5
Revises: de8434d88164
Create Date: 2024-08-07 12:55:46.554773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd60cdbabefe5'
down_revision = 'de8434d88164'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accesorios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('car1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('precio', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('accesorios_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('caracteristicas_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'accesorios', ['accesorios_id'], ['id'])
        batch_op.create_foreign_key(None, 'car1', ['caracteristicas_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('equipo', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('caracteristicas_id')
        batch_op.drop_column('accesorios_id')
        batch_op.drop_column('precio')

    op.drop_table('car1')
    op.drop_table('accesorios')
    # ### end Alembic commands ###
