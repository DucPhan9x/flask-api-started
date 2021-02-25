from models import Line


class LineRepository:
    @staticmethod
    def get(line_id):
        return Line.query.filter_by(line_id=line_id).first()

    def update(self, line_id, site_id, line_name):
        line = self.get(line_id)
        line.site_id = site_id
        line.line_name = line_name

        return line.save()

    @staticmethod
    def create(line_id, site_id, line_name):
        line = Line(line_id=line_id, site_id=site_id, line_name=line_name)

        return line.save()
