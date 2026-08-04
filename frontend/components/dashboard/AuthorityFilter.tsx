type Props = {
  authorities: string[];
  selected: string;
  onChange: (value: string) => void;
};

export default function AuthorityFilter({
  authorities,
  selected,
  onChange,
}: Props) {
  return (
    <div className="mt-8 flex justify-end">
      <select
        value={selected}
        onChange={(e) => onChange(e.target.value)}
        className="rounded-xl border bg-white px-4 py-3 shadow-sm"
      >
        {authorities.map((authority) => (
          <option
            key={authority}
            value={authority}
          >
            {authority}
          </option>
        ))}
      </select>
    </div>
  );
}