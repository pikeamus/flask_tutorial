"""posts to post

Revision ID: e7c810e7e6d6
Revises: 87731f940b3f
Create Date: 2019-08-18 15:15:23.383822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7c810e7e6d6'
down_revision = '87731f940b3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.drop_index('ix_posts_timestamp', table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_posts_timestamp', 'posts', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
