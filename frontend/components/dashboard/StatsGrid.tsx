import StatCard from "./StatCard";

type Props = {
  total: number;
  pending: number;
  critical: number;
  resolved: number;
};

export default function StatsGrid({
  total,
  pending,
  critical,
  resolved,
}: Props) {
  return (
    <div className="mt-10 grid gap-6 md:grid-cols-4">
      <StatCard
        title="AI Processed Today"
        value={total}
      />

      <StatCard
        title="Pending Incidents"
        value={pending}
      />

      <StatCard
        title="High-Priority Incidents"
        value={critical}
      />

      <StatCard
        title="Resolved Today"
        value={resolved}
      />
    </div>
  );
}