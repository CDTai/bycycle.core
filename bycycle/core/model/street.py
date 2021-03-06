from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import BigInteger, Boolean, Integer, String

from bycycle.core.geometry import DEFAULT_SRID, LineString, Point
from bycycle.core.geometry.sqltypes import LINESTRING
from bycycle.core.model import Base

from .intersection import Intersection


class Street(Base):

    __tablename__ = 'streets'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    osm_id = Column(BigInteger)
    osm_seq = Column(Integer)
    geom = Column(LINESTRING(DEFAULT_SRID))
    start_node_id = Column(BigInteger, ForeignKey(Intersection.id))
    end_node_id = Column(BigInteger, ForeignKey(Intersection.id))

    # Tags
    name = Column(String)
    highway = Column(String)
    bicycle = Column(String)
    cycleway = Column(String)
    foot = Column(String)
    sidewalk = Column(String)
    oneway = Column(Boolean)
    oneway_bicycle = Column(Boolean)

    start_node = relationship(
        Intersection, primaryjoin=(start_node_id == Intersection.id))
    end_node = relationship(
        Intersection, primaryjoin=(end_node_id == Intersection.id))

    @property
    def meters(self):
        return self.geom.reproject(DEFAULT_SRID, 2913).length

    @property
    def kilometers(self):
        return self.meters * 0.001

    @property
    def feet(self):
        return self.meters * 3.28084

    @property
    def miles(self):
        return self.meters * 0.000621371

    @property
    def display_name(self):
        return self.name or ('[%s]' % (self.highway or 'unknown'))

    def split(self, point, node_id, way1_id, way2_id):
        """Split this street at ``point``."""
        distance = self.geom.project(point)
        coords = self.geom.coords
        shared_coords = list(point.coords)

        coords1 = [coords[0]]
        coords2 = []

        for c in coords[1:-1]:
            p = Point(c)
            p_distance = self.geom.project(p)
            if p_distance < distance:
                coords1.append(c)
            elif p_distance > distance:
                coords2.append(c)

        coords2.append(coords[-1])

        coords1 = coords1 + shared_coords
        coords2 = shared_coords + coords2

        line1 = LineString(coords1)
        line2 = LineString(coords2)

        shared_node = Intersection(id=node_id, geom=point)

        # Start to shared node
        way1 = self.clone(
            id=way1_id,
            end_node_id=node_id,
            end_node=shared_node,
            geom=line1,
        )

        # Shared node to end
        way2 = self.clone(
            id=way2_id,
            start_node_id=node_id,
            start_node=shared_node,
            geom=line2,
        )

        shared_node.ways = [way1, way2]
        return shared_node, way1, way2

    def clone(self, **override_attrs):
        keys = [c.key for c in self.__mapper__.columns]
        keys += [r.key for r in self.__mapper__.relationships]
        attrs = {k: getattr(self, k) for k in keys}
        attrs.update(override_attrs)
        return self.__class__(**attrs)
