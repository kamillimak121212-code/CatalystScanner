from app.collectors.base.base_collector import (
    BaseCollector
)


class CollectorRegistry:

    def __init__(self):

        self._collectors = []

    def register(
        self,
        collector: BaseCollector
    ):

        self._collectors.append(
            collector
        )

        self._collectors.sort(
            key=lambda c: c.priority,
            reverse=True
        )

    def collectors(self):

        return list(
            self._collectors
        )

    def enabled_collectors(self):

        return [

            collector

            for collector in self._collectors

            if collector.enabled

        ]

    def __len__(self):

        return len(
            self._collectors
        )

    def __iter__(self):

        return iter(
            self._collectors
        )