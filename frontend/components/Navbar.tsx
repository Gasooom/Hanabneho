"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Navbar() {
  const pathname = usePathname();

  const linkClass = (href: string) =>
    `transition hover:text-blue-400 ${
      pathname === href
        ? "text-blue-500 font-semibold"
        : "text-slate-300"
    }`;

  return (
    <header className="sticky top-0 z-50 border-b border-slate-800 bg-slate-950/90 backdrop-blur">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-8">
        <Link
          href="/"
          className="text-2xl font-bold text-white"
        >
          Hanabneho
        </Link>

        <nav className="flex items-center gap-8">
          <Link href="/" className={linkClass("/")}>
            Home
          </Link>

          <Link
            href="/report"
            className={linkClass("/report")}
          >
            Report
          </Link>

          <Link
            href="/dashboard"
            className={linkClass("/dashboard")}
          >
            Dashboard
          </Link>
        </nav>

        <Link
          href="/report"
          className="rounded-lg bg-blue-600 px-5 py-2 font-medium text-white transition hover:bg-blue-700"
        >
          Analyze Now
        </Link>
      </div>
    </header>
  );
}