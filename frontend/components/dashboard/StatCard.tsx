type Props = {
  title: string;
  value: number | string;
};

export default function StatCard({
  title,
  value,
}: Props) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-sm">
      <p className="text-sm text-slate-500">
        {title}
      </p>

      <h2 className="mt-2 text-4xl font-bold text-slate-900">
        {value}
      </h2>
    </div>
  );
}