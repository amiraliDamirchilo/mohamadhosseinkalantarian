import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Mohamad Kalantarian — BIM Specialist & Revit Modeler',
  description:
    'Accurate Revit BIM models, point cloud to BIM, and custom parametric Revit families for architects and AEC teams.',
  openGraph: {
    title: 'Mohamad Kalantarian — BIM Specialist',
    description:
      'From drawings, designs, and point clouds to accurate, construction-ready Revit BIM models.',
    type: 'website',
    images: [
      {
        url: '/og.png',
        width: 1792,
        height: 1024,
        alt: 'Mohamad Kalantarian — BIM Specialist and Revit Modeler',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Mohamad Kalantarian — BIM Specialist',
    description:
      'From drawings, designs, and point clouds to accurate, construction-ready Revit BIM models.',
    images: ['/og.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
