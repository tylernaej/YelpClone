"""empty message

Revision ID: 7127891a65fb
Revises: 
Create Date: 2022-09-16 13:19:43.345688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7127891a65fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amenities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('businesses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('website', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('state', sa.String(length=50), nullable=False),
    sa.Column('zipcode', sa.String(length=50), nullable=False),
    sa.Column('country', sa.String(length=50), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=50), nullable=False),
    sa.Column('price_range', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('business_amenities',
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('amenity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['amenity_id'], ['amenities.id'], ),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
    sa.PrimaryKeyConstraint('business_id', 'amenity_id')
    )
    op.create_table('business_categories',
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('business_id', 'category_id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('review', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('uploader_id', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], ),
    sa.ForeignKeyConstraint(['uploader_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('reviews')
    op.drop_table('business_categories')
    op.drop_table('business_amenities')
    op.drop_table('businesses')
    op.drop_table('users')
    op.drop_table('categories')
    op.drop_table('amenities')
    # ### end Alembic commands ###
